import pandas as pd
from mcp.server.fastmcp import FastMCP
import numpy as np

# Initialize a pandas DataFrame with some data for temperature and flow rate
df = pd.DataFrame(
    {
        "temperature": np.random.normal(loc=80, scale=5, size=21),
        "flow_rate": np.random.normal(loc=15, scale=5, size=21),
    },
    index=pd.date_range(start="2023-01-01 00:00:00", periods=21, freq="15T")
)

mcp = FastMCP("Pump Telemetry", port=5003)

@mcp.tool(
        description="""
        Get telemetry data statistic for a physical measure on the pump.
        Measures must be either 'temperature' or 'flow_rate'.
        Statistic must be a valid pandas time-series aggregation function."""
)
def get_telemetry(measure: str, statistic: str) -> float:
    """Get telemetry data statistic for a measure"""
    # Check that measure is a valid column in the DataFrame
    if measure not in df.columns:
        raise ValueError(f"Invalid measure: {measure}. Must be one of {df.columns}")
    # Check that statistic is a valid pandas aggregation function
    valid_statistics = ["mean", "median", "min", "max", "sum", "std", "var", "sem", "skew", "kurt", "prod"]
    if statistic not in valid_statistics:
        raise ValueError(f"Invalid statistic: {statistic}. Must be one of {valid_statistics}")
    # Return the requested statistic for the specified measure
    return df[measure].agg(statistic)


if __name__ == "__main__":
    mcp.run(transport="sse")
