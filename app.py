import uvicorn
from fastapi import FastAPI, Request
from src.graphs.graph_builder import GraphBuilder
from src.llms.groq_llm import GroqLLM
from src.llms.nemotron import NemotronLLM

import os
from dotenv import load_dotenv
load_dotenv()
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

app = FastAPI()

@app.post("/blog")
async def create_blogs(request: Request):
    data = await request.json()
    topic = data.get('topic', '')
    
    startllm = NemotronLLM()
    llm = startllm.get_llm()

    graph_builder = GraphBuilder(llm)
    if topic:
        graph = graph_builder.setup_graph(usecase = 'topic')
        state = graph.invoke({'topic': topic})
        
    return {'data': state}

if __name__ == "__main__":
    uvicorn.run("app:app", host = "0.0.0.0", port = 8000, reload = True)