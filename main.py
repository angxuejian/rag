from app.graph import LLMNodeGraph


llm_graph = LLMNodeGraph()
graph = llm_graph.chatbot()

# llm_graph.show_graph()
# uvicorn main:app --host 127.0.0.1 --port 9000


def stream_graph_updates(user_input: str):
    for event in graph.stream(
        { "question": user_input} ,
        stream_mode="messages"     
        ):
        
        print(event[0].content, end="", flush=True)
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
