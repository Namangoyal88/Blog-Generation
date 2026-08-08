import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv


class NemotronLLM:
    def __init__(self):
        load_dotenv()
    
    def get_llm(self):
        try:
            os.environ["HF_TOKEN"] = hf_token = os.getenv("HF_TOKEN")
            hf_llm = HuggingFaceEndpoint(
                repo_id = 'nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16',
                huggingfacehub_api_token = hf_token,
                max_new_tokens = 2048,
                )
            llm = ChatHuggingFace(hf_llm)
            return llm
        except Exception as e:
            return ValueError(f"Error initializing Groq LLM: {e}")