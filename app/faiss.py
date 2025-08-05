from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from app.llm import LLM

class VECTOR_FAISS():
    
    def __init__(self):
        print('VECTOR FAISS => START')
        self.llm = LLM()
        self.embeddings = self.llm.embeddings()
        self.file_name = 'faiss_index'
        pass


    def save_local(self, docs: list[Document]):
        vectorstore = FAISS.from_documents(docs, self.embeddings)
        vectorstore.save_local(self.file_name)

    def similarity_search(self, question: str, k: int = 2):
        db = FAISS.load_local(self.file_name, self.embeddings, allow_dangerous_deserialization=True)
        return db.similarity_search(question, k=k)