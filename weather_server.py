from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather", port=5002)


@mcp.tool()
async def get_weather(location: str) -> int:
    """Get weather for location."""
    return f"Current conditions at {location}: Sunny, with light winds from the east. Temperature: 75°F"


if __name__ == "__main__":
    mcp.run(transport="sse")
