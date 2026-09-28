import argparse
import pathlib

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

from support_assistant.graph import build_graph


def main() -> None:
    load_dotenv()

    parser = argparse.ArgumentParser(description="Run the support assistant")
    parser.add_argument("prompt", help="The customer support request to answer")
    args = parser.parse_args()

    result = build_graph().invoke({"messages": [HumanMessage(content=args.prompt)]})
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()