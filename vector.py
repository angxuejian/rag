from app.text_splitter import TextSplitter
from app.faiss import VECTOR_FAISS
import os

def resolve_path(path: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, path)


text_splitter = TextSplitter()
vector_faiss = VECTOR_FAISS()

path = resolve_path('docs/button.md')
docs = text_splitter.load_md_chunks(path)

vector_faiss.save_local(docs)