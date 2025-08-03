from typing import List
from pydantic import BaseModel, Field
# from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_core.runnables import RunnableLambda
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import FAISS
from PIL import Image
from app.llm import LLM
from app.prompts import FILTER_TYPE_PROMPT, JAVASCRIPT_PROMPT, CSS_PROMPT, HTML_PROMPT, MULTIPLE_TYPE_PROMPT, VUE_PROMP
import io
import json


llm = LLM()

prompts = {
    'javascript': JAVASCRIPT_PROMPT,
    'css': CSS_PROMPT,
    'html': HTML_PROMPT
}

class State(BaseModel):
    messages: List[str] = Field(default_factory=list, metadata={"add_messages": True})
    question: str
    types: list[str] = Field(default_factory=list)
    prompt: str = ''


class LLMNodeGraph():
    def __init__(self):
        print('Graph => START')

        self.graph = None
        self.graph_builder = StateGraph(state_schema=State)

    
    def _filterType(self, state: State):

        chat = llm.ask()

        print('Filter type => START')
        result = chat.invoke([
            { "role": 'system', "content": FILTER_TYPE_PROMPT },
            { "role": "user", "content": state.question }
        ])
        
        content: list[str] = []

        if '[' in result.content and ']' in result.content:
            content = json.loads(result.content)
        elif result.content in ['css', 'javascript', 'html', 'vue']:
            content = [result.content]
        else: 
            content = []

        print("\n识别用户意图类型：", content, '\n')
        
        return state.model_copy(update={"types": content})
    
    def _route_by_type(self, state: State):
        types = state.types
        if len(types) == 0:
            return 'ai_answer'
        elif len(types) == 1:
            if state.types[0] == 'vue':
                return 'generate_vue_prompt'
            else:
                return 'generate_single_prompt'
        else:
            return 'generate_multiple_prompt'

    def _generateSinglePrompt(self, state: State):
        
        key = state.types[0]
        content = prompts.get(key)

        print(f'\n获取到{key}的prompt：', '\n')

        return state.model_copy(update={"prompt": content})


    def _generateMultiplePrompt(self, state: State):
        
        prompt = ''
        for item in state.types:
            prompt += (prompts.get(item) or "") + '\n'
        
        chat = llm.ask()
        result = chat.invoke([
            { "role": 'system', "content": MULTIPLE_TYPE_PROMPT },
            { "role": "user", "content": prompt }
        ])

        print('\n总结后的prompt：', result.content)

        return state.model_copy(update={"prompt": result.content})
    
    def _generateVuePrompt(self, state: State):
        embeddings = DashScopeEmbeddings(dashscope_api_key="", model='text-embedding-v4')
        db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
        results = db.similarity_search(state.question, k=2)

        p = ''
        print(results)
        for i, doc in enumerate(results, 1):
            content = doc.page_content.strip()
            meta = doc.metadata
            
            start_line = meta.get("start_line", "?")

            origin = f"【文档来源：第 {start_line} 行】"

            p += f"--- 段落 {i} ---\n{content}\n{origin}\n\n"

        prompt = VUE_PROMP.format(content=p)
        print('\nVue的prompt：', prompt)
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
        self.graph_builder.add_node('generate_single_prompt', RunnableLambda(self._generateSinglePrompt))
        self.graph_builder.add_node('generate_multiple_prompt', RunnableLambda(self._generateMultiplePrompt))
        self.graph_builder.add_node('generate_vue_prompt', RunnableLambda(self._generateVuePrompt))
        self.graph_builder.add_node('ai_answer', RunnableLambda(self._ai_answer))


        self.graph_builder.add_edge(START, 'filter_type')
        self.graph_builder.add_edge('generate_single_prompt', 'ai_answer')
        self.graph_builder.add_edge('generate_multiple_prompt', 'ai_answer')
        self.graph_builder.add_edge('generate_vue_prompt', 'ai_answer')

        self.graph_builder.add_edge('ai_answer', END)

        self.graph_builder.add_conditional_edges('filter_type', self._route_by_type, {
            "ai_answer": "ai_answer",
            "generate_single_prompt": "generate_single_prompt",
            "generate_multiple_prompt": "generate_multiple_prompt",
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





