from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv
load_dotenv()
llm = ChatOpenAI(
    model="gpt-4.1",
    api_key=os.getenv("OPENAI_API_KEY")
)

def ask_llm(prompt):
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content