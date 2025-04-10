AGENTS 
LLM lerin kendi düşünsün karar alabilsin gibi yapılar.
agents ların bir sürü tipleri var. langchaiin knedi desteklediği bir çok agint tipi var. biz ReACT KULLANACAĞIZ.
ReAct LLM lerle çalışırken kendi mantığıyla bizim kullnıdığımız araçları kullanalım mı kullanmayalım mı

ReAct in çalışması için bir araç kullanmamız gerekiyor. Tavily LLm lerimizi webe bağlamka için arç.aslında ücretli bir araç
1000 isteğe kadar ücretsiz kullanabiliyorsn.
endüstride kullanıyor.

bugününü hava durumunu sordum diyelim LLM bunu bilmiyor "TAVILY ile aratıp bunu kullanıcıya gösterebilirsin.

1-startTavily.py
google dan aramka gibi şu an LLm yok
![image](https://github.com/user-attachments/assets/c615facb-6b24-4a2a-a49d-b3819bf5f0b4)
![image](https://github.com/user-attachments/assets/c488e566-7d20-4461-90ec-977f4c9f89cf)

2
Travily ve LLM var
![image](https://github.com/user-attachments/assets/4c077ee5-8269-4bcc-8b3b-b401bc31ae00)

![image](https://github.com/user-attachments/assets/ef90a653-c7c0-4c70-864d-585d03393b4a)

page 4
4agentMemory.py hatası 
C:\Users\beyza\PycharmProjects\Langchain\Agents-Intro\.venv\Scripts\python.exe C:\Users\beyza\PycharmProjects\Langchain\Agents-Intro\4agentMemory.py 
>what is the weather in ankara right now?
Traceback (most recent call last):
  File "C:\Users\beyza\PycharmProjects\Langchain\Agents-Intro\4agentMemory.py", line 26, in <module>
    for chunk in agent_executor.stream(
                 ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\beyza\PycharmProjects\Langchain\Agents-Intro\.venv\Lib\site-packages\langgraph\pregel\__init__.py", line 1002, in stream
    next_checkpoint, next_tasks = _prepare_next_tasks(
                                  ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\beyza\PycharmProjects\Langchain\Agents-Intro\.venv\Lib\site-packages\langgraph\pregel\__init__.py", line 2019, in _prepare_next_tasks
    seen = checkpoint["versions_seen"][name]
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
KeyError: '__start__'

Process finished with exit code 1




