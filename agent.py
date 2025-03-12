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
    questions = [
        "what's (3 + 5) x 12?",
        "what is the weather in nyc?",
        "What is the average temperature of the pump?",
        "What is the median flow rate of the pump?",
        "What is the maximum temperature of the pump?",
        "What is the minimum flow rate of the pump?",
        "What is the standard deviation of the temperature of the pump?",
        "What is the variance of the flow rate of the pump?",
    ]

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
            "pump telemetry": {
                # make sure you start your telemetry server on port 5003
                "url": "http://localhost:5003/sse",
                "transport": "sse",
            },
        }
    ) as client:
        agent = create_react_agent(model, client.get_tools())
        for question in questions:
            response = await agent.ainvoke({"messages": question})
            print(response)


if __name__ == "__main__":
    asyncio.run(main())
