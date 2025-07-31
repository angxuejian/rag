from mcp.server.fastmcp import FastMCP
from app.graph import LLMNodeGraph


mcp = FastMCP('code-gen__server')

llm_graph = LLMNodeGraph()
graph = llm_graph.chatbot()

@mcp.tool()
def get_guide_code(user_input: str):
    """
    根据输入内容生成符合规范的 HTML、CSS 和 JavaScript 代码。

    参数：
        user_input(str): 输入内容，可以是完整代码、代码片段，或对代码的自然语言描述。

    返回值：
        str: 以代码块格式返回的规范化代码。
    """

    result = graph.invoke({ "question": user_input})

    return result['messages'].content


if __name__ == "__main__":
    print('code-gen__server => start')
    mcp.run(transport='stdio')
