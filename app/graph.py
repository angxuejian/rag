from typing import List
from pydantic import BaseModel, Field
from langgraph.graph import StateGraph, START, END
from langchain_core.runnables import RunnableLambda
from app.prompts import FILTER_TYPE_PROMPT, VUE_PROMP
from app.llm import LLM
from app.faiss import VECTOR_FAISS
from PIL import Image
import io

llm = LLM()
vector_faiss = VECTOR_FAISS()

class State(BaseModel):
    messages: List[str] = Field(default_factory=list, metadata={"add_messages": True})
    question: str
    type: str | None = None
    prompt: str = ''


class LLMNodeGraph():
    def __init__(self):
        print('Graph => START')

        self.graph = None
        self.graph_builder = StateGraph(state_schema=State)

    
    def _filterType(self, state: State):
        print('Filter type => START')

        chat = llm.ask()
        result = chat.invoke([
            { "role": 'system', "content": FILTER_TYPE_PROMPT },
            { "role": "user", "content": state.question }
        ])
        
        content = result.content
        print("识别用户意图类型：", content)
        
        return state.model_copy(update={"type": content})
    
    def _route_by_type(self, state: State):
        type = state.type
        if type == 'vue':
            return 'generate_vue_prompt'
        else:
            return 'ai_answer'

    
    def _generateVuePrompt(self, state: State):
        results = vector_faiss.similarity_search(state.question)

        p = ''
        print(results)
        for i, doc in enumerate(results, 1):
            content = doc.page_content.strip()
            meta = doc.metadata
            start_line = meta.get("start_line", "?")
            origin = f"【文档来源：第 {start_line} 行】"
            p += f"--- 段落 {i} ---\n{content}\n{origin}\n\n"

        prompt = VUE_PROMP.format(content=p)
        # print('Vue的prompt：', prompt)

        return state.model_copy(update={"prompt": prompt})

    def _ai_answer(self, state: State):

        chat = llm.ask()

        messages = chat.invoke([
            { "role": "system", "content": state.prompt },
            { "role": "user", "content": state.question }
        ])
        
        return state.model_copy(update={"messages": messages})


    def chatbot(self):
        self.graph_builder.add_node('filter_type', RunnableLambda(self._filterType))
        self.graph_builder.add_node('generate_vue_prompt', RunnableLambda(self._generateVuePrompt))
        self.graph_builder.add_node('ai_answer', RunnableLambda(self._ai_answer))

        self.graph_builder.add_edge(START, 'filter_type')
        self.graph_builder.add_edge('generate_vue_prompt', 'ai_answer')
        self.graph_builder.add_edge('ai_answer', END)

        self.graph_builder.add_conditional_edges('filter_type', self._route_by_type, {
            "ai_answer": "ai_answer",
            "generate_vue_prompt": "generate_vue_prompt"
        })

        self.graph = self.graph_builder.compile()
        return self.graph
    
    
    def show_graph(self):
        print('show_graph => START')
        if self.graph:
            png_data = self.graph.get_graph().draw_mermaid_png()
            img = Image.open(io.BytesIO(png_data))
            img.show()
            print('show_graph => SUCCESS')
        else:
            print('show_graph => Execute the "chatbot function" or "chatbot_tools function" first')





