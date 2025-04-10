"""from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.sqlite import SqliteSaver

load_dotenv()

model = ChatOpenAI(model="gpt-4")
memory = SqliteSaver.from_conn_string(":memory:")


search = TavilySearchResults(max_results=2)
tools = [search]

model_with_tools = model.bind_tools(tools)

agent_executor = create_react_agent(model, tools, checkpointer=memory)
config = {"configurable": {"thread_id": "abc123"}}#bu id bir database de tutulur genelde


if __name__ == '__main__':
    while True:
        user_input = input(">")
        for chunk in agent_executor.stream(
                {"messages": [HumanMessage(content=user_input)]}, config
        ):
            print(chunk)
            print("----")

#HATA VERİYOR
"""

from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4")
search = TavilySearchResults(max_results=2)

tools = [search]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

if __name__ == '__main__':
    response = agent.run("What is the weather in Ankara right now?")
    print(response)
