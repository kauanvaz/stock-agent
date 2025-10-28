from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langchain.agents import create_agent

from tools import get_company_info, get_current_stock_price, get_history_stock_price

load_dotenv()

model = ChatOpenAI(
    model='gpt-5-mini',
)

memory = MemorySaver() # Guarda a memória do chat

system_message = '''
Você é um agente analista financeiro e deve utilizar
suas ferramentas para responder o usuário.
'''

tools = [ # Ferramentas às quais o agente terá acesso
    get_company_info,
    get_current_stock_price,
    get_history_stock_price,
]

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
    for step in agent_executor.stream(
        {'messages': [input_message]}, config, stream_mode='values'
    ):
        step['messages'][-1].pretty_print()
