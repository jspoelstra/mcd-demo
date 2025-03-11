import asyncio
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import AzureChatOpenAI

load_dotenv()
model = AzureChatOpenAI(
    azure_deployment="gpt-4o-mini",
    api_version="2025-01-01-preview",
)


async def main():
    async with MultiServerMCPClient(
        {
            "math": {
                # make sure you start your math server on port 5001
                "url": "http://localhost:5001/sse",
                "transport": "sse",
            },
            "weather": {
                # make sure you start your weather server on port 5002
                "url": "http://localhost:5002/sse",
                "transport": "sse",
            },
        }
    ) as client:
        agent = create_react_agent(model, client.get_tools())
        math_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
        print(math_response)
        weather_response = await agent.ainvoke(
            {"messages": "what is the weather in nyc?"}
        )
        print(weather_response)


if __name__ == "__main__":
    asyncio.run(main())
