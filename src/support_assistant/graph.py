import os
from typing import Annotated, TypedDict

from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AnyMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages


class AssistantState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]


SYSTEM_PROMPT = """You are a helpful customer support assistant.
Answer clearly and ask for any information needed to help resolve the request."""


def build_graph(model: BaseChatModel | None = None):
    chat_model = model or ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-6-luna"),
        temperature=0,
    )

    def respond(state: AssistantState) -> dict[str, list[AnyMessage]]:
        reply = chat_model.invoke(
            [SystemMessage(content=SYSTEM_PROMPT), *state["messages"]]
        )
        return {"messages": [reply]}

    builder = StateGraph(AssistantState)
    builder.add_node("respond", respond)
    builder.add_edge(START, "respond")
    builder.add_edge("respond", END)
    return builder.compile()