import os
import asyncio
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient

async def main():
    # Get MATH_SERVER_URI from environment variable
    MCP_MATH_URI = os.getenv("MCP_MATH_URI", "http://localhost:5001/sse")
    print(f"MCP_MATH_URI: {MCP_MATH_URI}")

    # Create the client
    mcpc = MultiServerMCPClient(
        {
            "math": {
                # make sure you start your math server as specified in
                # the environment variable
                "url": MCP_MATH_URI,
                "transport": "sse",
            },
        }
    )
    
    # Connect to the servers by calling __aenter__ directly
    try:
        await mcpc.__aenter__()
    except Exception as e:
        raise e

    # Get the tools from the math server
    tools = mcpc.get_tools()
    print(tools)

    # When completely done, close connections
    await mcpc.__aexit__(None, None, None)

if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()
    # Go!
    asyncio.run(main())
