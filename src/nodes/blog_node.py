from langchain.messages import HumanMessage, SystemMessage
from src.states.blogstate import BlogState, Blog

class BlogNode:
    """ A class to represent the blog node """
    def __init__(self, llm):
        self.llm = llm


    def title_creation(self, state: BlogState) -> str:
        """ create the title for the blog """
        
        if 'topic' in state and state['topic']:
            prompt = """ you are an expert blog content writer. use markdown formatting.
            generate a blog title for the {topic}. this title should be creative and SEO friendly"""
            system_message = prompt.format(topic = state['topic'])
            response = self.llm.invoke(system_message)
            
            return {'blog': {'title': response.content}}
    
    
    def content_genetation(self, state: BlogState) -> str:
        """ generate the content for the blog """

        if 'topic' in state and state['topic']:
            prompt = """you are an expert blog content writer. use markdown formatting.
            generate a detailed blog content with detailed breakdown for the {topic}. """
            system_message = prompt.format(topic = state['topic'])
            response = self.llm.invoke(system_message)

            return {'blog': {'title': state['blog']['title'], 'content': response.content}}
        
        
    def route(self, state: BlogState) -> str:
        """ route the blog to the target language """
        return {'current_language': state['current_language']}
    
    def route_decision(self, state: BlogState) -> str:
        """ decide the target language for the blog """
        if state['current_language'] == 'hindi':
            return 'hindi'
        if state['current_language'] == 'german':
            return 'german'
                
        
    def translation(self, state: BlogState) -> str:
        """ translate the blog to the target language """
                
        translation_prompt = """
        Translate the following content into {current_language}.
        - Maintain the original tone, style and formatting.
        - adape culture references and idioms to be appropriate for {current_language}.
        Original content: {blog_content}
        """
        
        blog_content = state['blog']['content']
        messages = [HumanMessage(translation_prompt.format(current_language = state['current_language'], blog_content = blog_content))]
        
        translation_content = self.llm.invoke(messages)
        return translation_content