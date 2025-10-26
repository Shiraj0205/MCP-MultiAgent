from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
async def get_weather(location:str)->str:
    """    
    Args:
        location (str): _description_

    Returns:
        str: _description_
    """
    return f"Weather in {location} is sunny with 85F temperature."

if __name__=="__main__":
    # streamable HTTP transport. Interacts via HTTP requests
    mcp.run(transport="streamable-http")