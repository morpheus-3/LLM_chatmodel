from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Nanbeige/Nanbeige4.1-3B",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

chat_model = ChatHuggingFace(llm=llm)

response = chat_model.invoke("What is the capital of India?")
print(response.content)