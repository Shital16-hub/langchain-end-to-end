from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain.chat_models import init_chat_model

import os
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model("llama3-8b-8192", model_provider="groq")

messages = [
    SystemMessage("You are an expert in social media content strategy"),
    HumanMessage("Give a short tip to create engaging posts on Instagram"),
]

response = model.invoke(messages)
print(response.content)