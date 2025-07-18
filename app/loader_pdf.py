from langchain_community.document_loaders import PyPDFLoader
from llm import LLM
import asyncio
import os
import re
import requests



# proxies = {
#     'http': 'http:/10.144.1.10:8080',
#     'https': 'http://10.144.1.10:8080',
# }



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.path.join(BASE_DIR)

llm = LLM()

loader = PyPDFLoader('ali-guides.pdf')
pages = []

def load_pages():
    for page in loader.lazy_load():
        print(type(page.page_content))
        pages.append(page.page_content)

load_pages()
print(pages[0])

# for i, t in enumerate(pages):
#     print(len(t))
#     if len(t) > 10000:
#         print(f"第 {i} 条可能过长：{len(t)} 字符")
embedding = llm.embeddings()
print('开始')
vectors = embedding.embed_documents(pages[0])
print('结束')
print(vectors)

# llm.embeddings()