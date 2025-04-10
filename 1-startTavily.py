from dotenv import load_dotenv
# Tavily adlı arama motorunu kullanarak arama yapmayı sağlayan araç.
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()

# Tavily arama aracını oluşturuyoruz ve arama sonuçlarını 2 ile sınırlıyoruz.
search = TavilySearchResults(max_results=2)

# İstersek başka araçlar da oluşturabiliriz.
# Tüm araçları bir listeye koyuyoruz, bu liste daha sonra Agient/ajanımıza bağlanacak.
tools = [search]

#Şu an internete bağlanıp bir arama yapmış olduk
#LLM falan bağlamadık
#şu an düm düz goole a da istek atabilirdim
if __name__ == '__main__':
    search_results = search.invoke("what is the weather in istanbul?")
    print(search_results)