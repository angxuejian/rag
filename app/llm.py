from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from typing import List
from app.config import llm

class LLM():

    def __init__(self):
        print('LLM => START')
        pass
    
    def config(self, type: str):
        if not type:
            raise ValueError("type is empty")
        
        if (type == 'qwen'):
            return ChatOpenAI(
                openai_api_key=llm.get("openai_api_key"),
                openai_api_base=llm.get("openai_api_base"),
                model_name=llm.get("model_name"),
                request_timeout=10,
                streaming=True
            )
        elif (type == 'emdeddings'):
            return OpenAIEmbeddings(
                openai_api_key=llm.get("openai_api_key"),
                openai_api_base=llm.get("openai_api_base"),
                model="text-embedding-v4",
                dimensions=1024,
                model_kwargs={
                    "encoding_format": "float",
                },
                request_timeout=60
            )

    def ask(self):

        print('\n selected ask llm')
        return self.config('qwen')
    
    def embeddings(self):
        print('selected embedding llm')
        return self.config('emdeddings')

    def ask_tools(self, tools: List):

        print('selected ask tools llm')
        return self.config('qwen').bind_tools(tools)