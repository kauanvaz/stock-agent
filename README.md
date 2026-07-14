# Stock Agent

Stock Agent is a small Python project that provides an interactive financial analysis assistant. It uses OpenAI through LangChain/LangGraph and stock-market data from yfinance, either through local LangChain tools or through an MCP server configuration.

The agent is designed to answer user questions about companies, current stock prices, and historical stock prices by selecting the appropriate tool during the conversation.

## Technologies

- Python
- LangChain and LangGraph for agent orchestration
- OpenAI chat models through `langchain-openai`
- yfinance for stock and company data
- MCP through `langchain-mcp-adapters` for remote or local tool servers

## Project Structure

```text
.
├── simple_agent.py    # Interactive agent using local yfinance tools
├── mcp_agent.py       # Interactive agent using tools loaded from MCP
├── tools.py           # LangChain tool definitions backed by yfinance
├── mcp_servers.py     # MCP server configuration
├── requirements.txt   # Python dependencies
└── .env.example       # Example environment variables
```

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a local environment file:

```bash
cp .env.example .env
```

Then edit `.env` and set your API keys:

```env
OPENAI_API_KEY=your_openai_api_key
SMITHERY_API_KEY=your_smithery_api_key
```

`OPENAI_API_KEY` is required for both agents. `SMITHERY_API_KEY` is only needed if you enable the Smithery MCP configuration in `mcp_servers.py`.

## Running the Project

Run the direct yfinance agent:

```bash
python simple_agent.py
```

Run the MCP-backed agent:

```bash
python mcp_agent.py
```

Both commands start an interactive prompt. Type a question such as:

```text
What is the current price of AAPL?
```

## MCP Configuration

The active MCP configuration currently points to a deployed FastMCP Cloud yfinance server:

```python
'url': 'https://mcp-yfinance.fastmcp.app/mcp'
```

Alternative Smithery, local HTTP, and local STDIO configurations are included as commented examples in `mcp_servers.py`.

