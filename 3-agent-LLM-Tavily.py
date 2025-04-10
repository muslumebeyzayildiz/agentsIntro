from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI


load_dotenv()

# GPT-4 modelini başlat
llm = ChatOpenAI(model="gpt-4")

# Tavily arama aracını tanımla
search = TavilySearchResults(max_results=2)

# Araçları listeye al
tools = [search]

# ReAct ajanını başlat (LangChain Agent framework)
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # ReAct tabanlı davranış
    verbose=True
)

# Ajanı çalıştır
if __name__ == '__main__':
    response = agent.run("What's the weather in Istanbul?")
    print(response)