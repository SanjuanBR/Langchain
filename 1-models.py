import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


load_dotenv()

chat = ChatOpenAI(model="gpt-5-nano")

# prompt = 'Conte uma história sobre aprendizado de máquina em menos de 50 palavras'
#
# for chunk in chat.stream([HumanMessage(content=prompt)]):
#     print(chunk.content, end="", flush=True)


# questions = [
#     "O que é memória ram?",
#     "O que é disco rígido?",
#     "o que é processador?"]
#
# answer = chat.batch(questions)
# print(answer)


