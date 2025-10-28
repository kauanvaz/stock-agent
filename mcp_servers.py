import os
from dotenv import load_dotenv

load_dotenv()

SMITHERY_API_KEY = os.getenv('SMITHERY_API_KEY')

MCP_SERVERS_CONFIG = {
    # 'yfinance': { # MCP da Smithery
    #     'url': f'https://server.smithery.ai/@pycodebr/yahoo-finance-mcp/mcp?api_key={SMITHERY_API_KEY}',
    #     'transport': 'streamable_http',
    # },
    # 'yfinance': { # MCP local com HTTP
    #     'url': 'http://localhost:8001/mcp',
    #     'transport': 'streamable_http',
    # },
    # 'yfinance': { # MCP local com STDIO
    #     'command': 'python',
    #     'args': ['/mnt/c/Users/User/Downloads/CODIGOS_MODULO_10/mcp_server/main.py'],
    #     'transport': 'stdio',
    # },
    'yfinance': { # MCP deployado no FastMCP Cloud
        'url': 'https://mcp-yfinance.fastmcp.app/mcp',
        'transport': 'streamable_http',
    },
}
