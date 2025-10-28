import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langchain.agents import create_agent

from mcp_servers import MCP_SERVERS_CONFIG

async def main(): # get_tools é uma função assíncrona, então main também deve ser assíncrona
    model = ChatOpenAI(model='gpt-5-mini')
    memory = MemorySaver() # Guarda a memória do chat

    mcp_client = MultiServerMCPClient(MCP_SERVERS_CONFIG)
    tools = await mcp_client.get_tools()

    system_message = '''
    Você é um agente analista financeiro e deve utilizar
    suas ferramentas para responder o usuário.
    '''

    agent_executor = create_agent(
        model=model,
        tools=tools,
        system_prompt=system_message,
        checkpointer=memory,
    )

    # Separa as threads de conversa na memória
    config = {'configurable': {'thread_id': '1'}}

    while True:
        input_message = {
            'role': 'user',
            'content': input('Digite: '),
        }
        async for step in agent_executor.astream(
            {'messages': [input_message]}, config, stream_mode='values'
        ):
            step['messages'][-1].pretty_print()


asyncio.run(main()) # Executa a função principal assíncrona
