from langchain_core.language_models.fake_chat_models import FakeListChatModel
from langchain_core.messages import HumanMessage

from support_assistant.graph import build_graph


def test_graph_returns_model_response() -> None:
    graph = build_graph(FakeListChatModel(responses=["I can help with that."]))

    result = graph.invoke(
        {"messages": [HumanMessage(content="My order arrived damaged.")]}
    )

    assert result["messages"][-1].content == "I can help with that."