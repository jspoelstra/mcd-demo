from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field

mcp = FastMCP("Math", port=5001)
class MathRequest(BaseModel):
    a: int = Field(..., description="The first number")
    b: int = Field(..., description="The second number")

@mcp.tool()
def add(request: MathRequest) -> int:
    """Add two numbers

    Returns:
        int: The sum of a and b
    """
    return request.a + request.b


@mcp.tool()
def multiply(request: MathRequest) -> int:
    """Multiply two numbers
            
    Returns:
        int: The product of a and b
    """
    return request.a * request.b

class DivRequest(BaseModel):
    a: int = Field(..., description="Numerator")
    b: int = Field(..., description="Denominator")

@mcp.tool()
def divide(request: DivRequest) -> float:
    """This function performs division of two integers and returns the result as a float.        
    Returns:
        float: The result of dividing a by b
        
    Raises:
        ValueError: If b is zero
    """
    if request.b == 0:
        raise ValueError("Cannot divide by zero")
    return request.a / request.b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers
    
    Args:
        a (int): The number to subtract from
        b (int): The number to subtract
        
    Returns:
        int: The result of a minus b
    """
    return a - b

@mcp.tool()
def power(a: int, b: int) -> int:
    """Raise a number to the power of another
    
    Args:
        a (int): The base number
        b (int): The exponent
        
    Returns:
        int: The result of a raised to the power of b
    """
    return a ** b

@mcp.tool()
def factorial(n: int) -> int:
    """Calculate the factorial of a number
    
    Args:
        n (int): The non-negative integer to calculate factorial for
        
    Returns:
        int: The factorial of n (n!)
        
    Raises:
        ValueError: If n is negative
    """
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
    """Calculate the nth Fibonacci number
    
    Args:
        n (int): The non-negative integer position in the Fibonacci sequence
        
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
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
