from app.graph import LLMNodeGraph
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.responses import PlainTextResponse
import asyncio

app = FastAPI()
llm_graph = LLMNodeGraph()

graph = llm_graph.chatbot()

# llm_graph.show_graph()


# uvicorn main:app --host 127.0.0.1 --port 9000

async def fake_stream(user_input: str):
    # for chunk in graph.stream({ "question": user_input}):
    #     yield f"event: chat\ndata: {chunk}\n\n"
    chunks = []
    for chunk in graph.stream({"question": user_input}, stream_mode="messages"):
        chunks.append(chunk)
    full_result = "".join(chunks[0].content)
    return PlainTextResponse(full_result)


@app.get("/stream")
async def stream(user_input: str):

    return fake_stream(user_input)
    # return StreamingResponse(fake_stream(user_input), media_type="text/event-stream")





def stream_graph_updates(user_input: str):
    print('user_input', user_input)

    # result = graph.invoke({ "question": user_input})
    # print('\n result：', result['messages'][0].content)
    # content = ''
    for event in graph.stream(
        { "question": user_input} ,
        stream_mode="messages"     
        ):
        
        print(event[0].content, end="", flush=True)
        # delta = event[0].content
        # if delta:
        #     content += delta
        #     # print(delta, end="", flush=True)
    print('\n\n')
 
while True:
    try:
        
        user_input = input("User(quit、exit、q): ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        stream_graph_updates(user_input)
    except Exception as e:
        print(e)
        print("Exit goodbye!")
        break
