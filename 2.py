from dotenv import load_dotenv

# Tavily adlı arama motorunu kullanarak arama yapmayı sağlayan araç.
from langchain_community.tools.tavily_search import TavilySearchResults

# OpenAI'nin GPT modellerini LangChain üzerinden kullanmak için ChatOpenAI sınıfı.
from langchain_openai import ChatOpenAI

# Kullanıcıdan gelen mesajları temsil eden sınıf.
from langchain_core.messages import HumanMessage

# LangGraph paketinde önceden tanımlı bir ReAct ajanı oluşturmak için kullanılır.
from langgraph.prebuilt import create_react_agent

load_dotenv()

model = ChatOpenAI(model="gpt-4")

# Tavily arama aracını oluşturuyoruz ve arama sonuçlarını 2 ile sınırlıyoruz.
search = TavilySearchResults(max_results=2)

# İstersek başka araçlar da oluşturabiliriz.
# Tüm araçları bir listeye koyuyoruz, bu liste daha sonra Agient/ajanımıza bağlanacak.
tools = [search]

# Oluşturduğumuz modeli, araçları kullanabilir hale getiriyoruz.
model_with_tools = model.bind_tools(tools)

if __name__ == '__main__':
    # Ajanı çalıştırıyoruz ve kullanıcıdan gelen mesajı içeren bir sözlük veriyoruz.
    response = model_with_tools.invoke(
        [HumanMessage(content="whats the weather in istanbul?")]
    )#liste içinde yollaamız gerekiyor
    # Dönen yanıtın içindeki "messages" kısmını yazdırıyoruz.
    print(response)
    print(response.tool_calls)#bizim verdiğimiz listedewki araçalrın ne kadar kullanıldığını gösteriyor.
    # content="hi" olunca
    #
    # [] boş geldi. çünkü LLm kendi karar veriyor şuan. TAVILY kullanılmadı

    # content="whats the weather in istanbul?") istanbl olunca kullanmış oldu
    # content='' cevap boş geliyor
    # ['tavily_search_results_json'....] bunu d akullanıyor aslında

#agent olmadan tam istediğimiz sonucu alamadık






