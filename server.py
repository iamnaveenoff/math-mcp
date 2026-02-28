from fastapi import FastAPI, Request
from mcp.server.fastapi import FastAPIMCP

app = FastAPI()
mcp = FastAPIMCP(app, name="math-python-mcp")

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> float:
    return a / b