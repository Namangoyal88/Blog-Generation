from langgraph.graph import StateGraph, START, END
from src.llms.groq_llm import GroqLLM
from src.llms.nemotron import NemotronLLM
from src.llms.google_llm import GoogleLLM
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
    
    
    def build_language_graph(self):
        """ Build a graph for blog generation with inputs topic and language """
    
        self.blog_node_obj = BlogNode(self.llm)
        self.graph.add_node('title_creation', self.blog_node_obj.title_creation)
        self.graph.add_node('content_generation', self.blog_node_obj.content_genetation)
        self.graph.add_node('route', self.blog_node_obj.route)
        self.graph.add_node('hindi_translation', lambda state: self.blog_node_obj.translation({**state, 'current_language': 'hindi'}))
        self.graph.add_node('german_translation', lambda state: self.blog_node_obj.translation({**state, 'current_language': 'german'}))
        
        self.graph.add_edge(START, 'title_creation')
        self.graph.add_edge('title_creation', 'content_generation')
        self.graph.add_edge('content_generation', 'route')
        self.graph.add_conditional_edges(
            'route', 
            self.blog_node_obj.route_decision, 
            {'hindi': 'hindi_translation', 'german': 'german_translation'}
            )
        self.graph.add_edge('hindi_translation', END)
        self.graph.add_edge('german_translation', END)
        return self.graph
    
    
    def setup_graph(self, usecase):
        if usecase == 'topic':
            self.graph = self.build_topic_graph()
        elif usecase == 'language':
            self.graph = self.build_language_graph()
        else:
            raise ValueError(f'Invalid usecase {usecase}')
        return self.graph.compile()


llm = GoogleLLM().get_llm()
graph_builder = GraphBuilder(llm)
graph = graph_builder.build_language_graph().compile()