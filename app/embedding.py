from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from langchain.text_splitter import MarkdownHeaderTextSplitter
import os


def resolve_path(path: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, path)


def load_md_semantic_chunks(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.splitlines()
    splitter = MarkdownHeaderTextSplitter(headers_to_split_on=[("#", "H1"), ("##", "H2"), ("###", "H3")])
    docs = [doc for doc in splitter.split_text(content) if doc.page_content.strip()]

    # 为每个块加上起始行号
    for doc in docs:
        chunk = doc.page_content.strip()
        start_line = None
        if chunk:
            for idx, line in enumerate(lines, 1):
                if line.strip() and chunk.startswith(line.strip()):
                    start_line = idx
                    break
        doc.metadata["start_line"] = start_line
    return docs

docs = load_md_semantic_chunks(resolve_path('front_guide.md'))

# print(docs)


# docs = [
#     Document(page_content="今天上海的天气很好，阳光明媚"),
#     Document(page_content="北京今天下雨了"),
#     Document(page_content="昨天的气温很低，只有5度"),
#     Document(page_content="明天可能会有台风"),
# ]

embeddings = DashScopeEmbeddings(dashscope_api_key="", model='text-embedding-v4')




# 向量化 + 本地保存
# vectorstore = FAISS.from_documents(docs, embeddings)
# vectorstore.save_local("faiss_index")



# 查询
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

query = "帮我写个节流函数"
print('\n\n', query)
results = db.similarity_search(query, k=1)

print(results)
for doc in results:
    print(doc.page_content)

# 1. 定一个文档，文本切割
# 2. 默认向量搜索、试一下混合搜索
# 3. 最好展示文档页码和出处
