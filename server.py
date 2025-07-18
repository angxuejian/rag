from mcp.server.fastmcp import FastMCP
import httpx
import asyncio
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

    # result = graph.invoke({ "question": user_input})


    # return result['messages'][0].content

    # try:
    #     async with httpx.AsyncClient() as client:
    #         response = await client.get(
    #             "http://152.136.45.29:8008/stream",
    #             params={"user_input": user_input}
    #         )
    #     if response.status_code == 200:
    #         data = response.json()
    #         return data
    #     else:
    #         return None
    try:
        with httpx.Client() as client:
            response = client.get(
                "http://152.136.45.29:8008/stream",
                params={"user_input": user_input}
            )
            print(response.text)

        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        return f'服务器调用失败: {str(e)}'



if __name__ == "__main__":
    print('code-gen__server => start')
    mcp.run(transport='stdio')
    # print("✅ MCP 工具服务启动中 (http)...")
    # mcp.run(transport="http", host="127.0.0.1", port=9010)