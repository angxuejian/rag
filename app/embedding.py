from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document

docs = [
    Document(page_content="今天上海的天气很好，阳光明媚"),
    Document(page_content="北京今天下雨了"),
    Document(page_content="昨天的气温很低，只有5度"),
    Document(page_content="明天可能会有台风"),
]

embeddings = DashScopeEmbeddings(dashscope_api_key="", model='text-embedding-v4')

# 向量化 + 本地保存
# vectorstore = FAISS.from_documents(docs, embeddings)
# vectorstore.save_local("faiss_index")



# 查询
# db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# query = "上海天气怎么样"
# print('\n\n', query)
# results = db.similarity_search(query, k=3)

# print(results)
# for doc in results:
#     print(doc.page_content)

# 1. 定一个文档，文本切割
# 2. 默认向量搜索、试一下混合搜索
# 3. 最好展示文档页码和出处
