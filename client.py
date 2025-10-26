from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

import asyncio
import os

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")


async def main():
    """_summary_
    """
    client = MultiServerMCPClient(
        
        {
            "calculator":{
                "command":"python",
                 "args":["calculator.py"],
                  "transport":"stdio"
                 
                },
            
            
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http"
                
            }
            
        }
        
    )
    tools = await client.get_tools()
    
    #model = ChatGroq(model="deepseek-r1-distill-llama-70b")
    model = ChatGroq(model="llama-3.1-8b-instant")
    
    agent = create_react_agent(model, tools)
    # agent = AgentExecutor.from_agent_and_tools(
    #     agent=create_json_chat_agent(llm=model, tools=tools),
    #     tools=tools,
    #     handle_parsing_errors=True
    # )
    
    response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    )

    # response = await agent.ainvoke(
    #     {"messages": [{"role": "user", "content": "Get weather in Paris?"}]}
    # )
    
    print(response["messages"][-1].content)



asyncio.run(main())