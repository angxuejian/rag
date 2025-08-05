from mcp.server.fastmcp import FastMCP
from app.graph import LLMNodeGraph


mcp = FastMCP('rag__server')

llm_graph = LLMNodeGraph()
graph = llm_graph.chatbot()

@mcp.tool()
def get_value(user_input: str):
    """
    根据用户输入，从知识库中检索相关信息并返回规范化代码。

    参数:
        user_input (str): 用户输入内容，可以是完整代码、代码片段，或对代码的自然语言描述。

    返回:
        str: 模型基于知识库生成的规范化代码，以代码块形式返回。
    """

    try:
        result = graph.invoke({ "question": user_input })
        return result['messages'].content
    except Exception as e:
        return f"调用知识库失败：{str(e)}"


if __name__ == "__main__":
    print('rag__server => start')
    mcp.run(transport='stdio')
