from langchain_openai import ChatOpenAI
from langchain_community.embeddings import DashScopeEmbeddings
from typing import List
from app.config import llm, embedding, rerank
import dashscope

class LLM():

    def __init__(self):
        print('LLM => START')
        pass
    
    def config(self, type: str):
        if not type:
            raise ValueError("type is empty")
        
        if (type == 'qwen'):
            return ChatOpenAI(
                openai_api_key=llm.get("api_key"),
                openai_api_base=llm.get("api_base"),
                model_name=llm.get("model_name"),
                request_timeout=10,
                streaming=True
            )
        elif (type == 'emdeddings'):
            return DashScopeEmbeddings(
                dashscope_api_key=embedding.get("api_key"),
                model=embedding.get("model_name")
            )
        elif (type == 'rerank'):

            def create_rerank(query: str, documents: List[str]):
                return dashscope.TextReRank.call(
                    api_key=rerank.get("api_key"),
                    model=rerank.get("model_name"),
                    query=query,
                    documents=documents,
                    top_n=3,
                    return_documents=True
                )
            
            return create_rerank

    def ask(self):
        print('selected ask llm')
        return self.config('qwen')
    
    def embeddings(self):
        print('selected embedding llm')
        return self.config('emdeddings')
    
    def rerank(self, query: str, documents: List[str]):
        print('selected rerank llm')
        return self.config('rerank')(query=query, documents=documents)

    def ask_tools(self, tools: List):
        print('selected ask tools llm')
        return self.config('qwen').bind_tools(tools)