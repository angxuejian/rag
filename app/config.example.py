
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
