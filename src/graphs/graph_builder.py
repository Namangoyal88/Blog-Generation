from langgraph.graph import StateGraph, START, END
from src.llms.groq_llm import GroqLLM
from src.llms.nemotron import NemotronLLM
from src.states.blogstate import BlogState
from src.nodes.blog_node import BlogNode


class GraphBuilder:
    def __init__(self, llm: GroqLLM):
        self.llm = llm
        self.graph = StateGraph(BlogState)
    
    def build_topic_graph(self) -> StateGraph:
        """ Build a graph to generate blogs based on a topic """
        
        self.blog_node_obj = BlogNode(self.llm)
        self.graph.add_node('title_creation', self.blog_node_obj.title_creation)
        self.graph.add_node('content_generation', self.blog_node_obj.content_genetation)
        self.graph.add_edge(START, 'title_creation')
        self.graph.add_edge('title_creation', 'content_generation')
        self.graph.add_edge('content_generation', END)
        
        return self.graph
    
    def setup_graph(self, usecase):
        if usecase == 'topic':
            self.graph = self.build_topic_graph()
        else:
            raise ValueError(f'Invalid usecase {usecase}')
        return self.graph.compile()


llm = NemotronLLM().get_llm()
graph_builder = GraphBuilder(llm)
graph = graph_builder.build_topic_graph().compile()