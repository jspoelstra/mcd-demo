from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math", port=5001)


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b

@mcp.tool()
def power(a: int, b: int) -> int:
    """Raise a number to the power of another"""
    return a ** b

@mcp.tool()
def factorial(n: int) -> int:
    """Calculate the factorial of a number"""
    if n < 0:
        raise ValueError("Cannot calculate factorial of negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

@mcp.tool()
def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number"""
    if n < 0:
        raise ValueError("Cannot calculate Fibonacci of negative numbers")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    mcp.run(transport="sse")
