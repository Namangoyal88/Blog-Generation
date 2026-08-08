from langgraph.graph import StateGraph, START, END
from src.llms.groq_llm import GroqLLM
from src.llms.nemotron import NemotronLLM
from src.states.blogstate import BlogState


class GraphBuilder:
    def __init__(self, llm: GroqLLM):
        self.llm = llm
        self.graph = StateGraph()
    
    def build_topic_graph(self) -> StateGraph:
        """ Build a graph to generate blogs based on a topic """
        self.graph.add_node('title_creation',)
        self.graph.add_node('content_generation')
        self.graph.add_edge(START, 'title_generation')
        self.graph.add_edge('title_generation', 'content_generation')
        self.graph.add_edge('content_generation', END)
        
        return self.graph