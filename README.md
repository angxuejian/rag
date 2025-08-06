# rag

rag prototype


## Features

1. text splitter: markdown
2. vector database: FAISS
3. local mcp tool
4. langgraph workflow


## Large language model

1. [qwen-max](https://bailian.console.aliyun.com/?spm=5176.29597918.J_SEsSjsNv72yRuRFS2VknO.2.343e7b08K1DeQL&tab=model#/model-market/detail/qwen-max?modelGroup=qwen-max)

2. [text-embedding-v4](https://bailian.console.aliyun.com/?spm=5176.29597918.J_SEsSjsNv72yRuRFS2VknO.2.343e7b08K1DeQL&tab=model#/model-market/detail/text-embedding-v4)

3. [gte-rerank-v2](https://bailian.console.aliyun.com/?spm=5176.29597918.J_SEsSjsNv72yRuRFS2VknO.2.343e7b08K1DeQL&tab=model#/model-market/detail/gte-rerank-v2)

## Installation

1、clone repository

```bash
git clone https://github.com/angxuejian/rag.git
```

2、install

```bash
pip install -r requirements.txt
```

## Config

1、在app目录下创建config.py文件 (可从config.example.py文件复制)

2、添加API密钥，可申请[百炼LLM](https://bailian.console.aliyun.com/?tab=model#/model-market)，均有免费Token使用

```python
# Global LLM configuration
# 阿里云百炼 https://bailian.console.aliyun.com/?tab=model#/model-market
llm = {
    "api_key": "YOUR_API_KEY",
    "api_base": 'https://dashscope.aliyuncs.com/compatible-mode/v1',
    "model_name": 'qwen-max'  # 根据千问文档选择合适的模型，例如 qwen-turbo 或 qwen-plus
}

embedding = {
    'api_key': "YOUR_API_KEY",
    "model_name": "text-embedding-v4"
}

rerank = {
    "api_key": "YOUR_API_KEY",
    "model_name": "gte-rerank-v2"
}
```

## Run

1、运行 vector.py 在本地创建向量数据库，默认会使用`docs/button.md`文件，可修改为自己的`md`文件

> 当前默认 `prompt` 是与 `docs/buttom.md` 相对应，如修改 `md` 文件别忘了修改 `prompt`

```python
python vector.py
```

2、大模型和本地向量数据库配置完成后，即可运行查看效果 ~

```python
python main.py
```

3、使用 MCP TOOL，可参考 `.vscode/mcp.json` 将其路径改为真实路径，即可使用。

## 交流

可通过 ✉️ 邮箱联系 @angxuejian: xuejian.ang@gmail.com

or [Issues](https://github.com/angxuejian/rag/issues)

希望 rag 可以帮助你快速了解 + 上手AI应用😎