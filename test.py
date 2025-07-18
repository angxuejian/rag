import httpx
import asyncio


def get_guide_code():
    print('123')
    try:
        with httpx.Client() as client:
            print('?')
            response = client.get(
                "http://152.136.45.29:8008/stream",
                params={"user_input": '帮我写个节流函数'}
            )
            print(response.text)

        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        print(e, '1')
        return f'服务器调用失败: {str(e)}'



get_guide_code()