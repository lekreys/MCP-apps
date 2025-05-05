import asyncio

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from mcp_use import MCPAgent , MCPClient
from dotenv import load_dotenv


load_dotenv()

apikey = os.getenv("OPENAI_API_KEY")



class connection_start : 


    def __init__(self):

        self.config_file = r"server.json"
        self.client = MCPClient.from_dict(self.config_file)
        self.llm = ChatOpenAI(model="gpt-4o" , api_key=apikey)

        self.agent = MCPAgent(
            llm = self.llm,
            client=self.client,
            max_steps=15,
            memory_enabled=True
         )

    
    async def get_chat(self, user_input) :

        """Run a chat using MCPAgent buit-in conversation memory"""
    
        try:
            response = await self.agent.run(user_input)
            return response

        except Exception as e : 
            return f"\n error : {e}"
        
    
    def get_chat_sync(self, user_input):

        return asyncio.run(self.get_chat(user_input))
        
    

        

                