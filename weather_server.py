from mcp.server.fastmcp import FastMCP
import random

mcp = FastMCP("Weather", port=5002)

conditions = ["sunny", "cloudy", "rain", "snow", "windy", "foggy"]
wind_strengths = ["light", "moderate", "strong"]
directions = [
    "north",
    "northeast",
    "east",
    "southeast",
    "south",
    "southwest",
    "west",
    "northwest",
]


@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location."""
    condition = random.choice(conditions)
    wind_strength = random.choice(wind_strengths)
    direction = random.choice(directions)
    temperature = random.randint(30, 100)  # Temperature in Fahrenheit
    return f"Current conditions at {location}: {condition.capitalize()}, with {wind_strength} winds from the {direction}. Temperature: {temperature}°F"


if __name__ == "__main__":
    mcp.run(transport="sse")
