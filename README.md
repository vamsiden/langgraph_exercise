# LangGraph Interview Exercise

A small, ready-to-run LangChain and LangGraph starter for a coding interview exercise. The included example is a support-request assistant; candidates can extend the graph with routing, tools, memory, or structured output.

## Setup

Requires Python 3.11 or newer. Create and activate a virtual environment, then install the project:

```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

Copy `.env.example` to `.env` and add an OpenAI API key to run the assistant:

```text
OPENAI_API_KEY=your-key
OPENAI_MODEL=gpt-4o-mini
```

Run the example:

```powershell
python -m support_assistant.cli "My order arrived damaged. What should I do?"
```

Run tests (no API key required):

```powershell
pytest
```

## Exercise

The starter graph sends the conversation to a chat model and returns its response. A useful interview prompt is to ask the candidate to classify each request as `billing`, `technical`, or `other`, then route it to a specialist node while preserving the conversation state. The fake-model test demonstrates how to test graph behavior without network access or credentials.

The graph and state live in `src/support_assistant/graph.py`; the command-line entry point is in `src/support_assistant/cli.py`.
