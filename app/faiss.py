from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from app.llm import LLM

class VECTOR_FAISS():
    
    def __init__(self):
        print('VECTOR FAISS => START')
        self.llm = LLM()
        self.file_name = 'faiss_index'
        pass


    def save_local(self, docs: list[Document]):
        vectorstore = FAISS.from_documents(docs, self.llm.embeddings())
        vectorstore.save_local(self.file_name)