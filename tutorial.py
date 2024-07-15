from typing import Annotated, Literal
from typing_extensions import TypedDict

from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")


class State(TypedDict):
    messages: Annotated[list, add_messages]
    api_call_count: int


def chatbot(state: State):
    if not state["api_call_count"]:
        state["api_call_count"] = 0
    state["api_call_count"] += 1
    return {
        "messages": [llm.invoke(state["messages"])],
        "api_call_count": state["api_call_count"],
    }


graph = StateGraph(State)

graph.add_node("chatbot", chatbot)
graph.set_entry_point("chatbot")
graph.set_finish_point("chatbot")
runner = graph.compile()

response = runner.invoke({"messages": ["こんにちは"], "api_call_count": 1})
print(response["messages"][-1].content)
