import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


class GoogleLLM:
    def __init__(self):
        load_dotenv()
    
    def get_llm(self):
        try:
            os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
            llm = ChatGoogleGenerativeAI(
            model = "gemini-3.6-flash",
            temperature = 0.7)
            return llm
        
        except Exception as e:
            raise ValueError(f"Error initializing Google LLM: {e}")