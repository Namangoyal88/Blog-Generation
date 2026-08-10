import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv



class GroqLLM:
    def __init__(self):
        load_dotenv()
    
    def get_llm(self):
        try:
            os.environ["GROQ_API_KEY"] = groq_api_key = os.getenv("GROQ_API_KEY")
            llm = ChatGroq(api_key = groq_api_key, model = 'openai/gpt-oss-120b')
            return llm
        except Exception as e:
            raise ValueError(f"Error initializing Groq LLM: {e}")