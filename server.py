from fastapi import FastAPI
from mcp.server.fastapi import FastAPIMCP

app = FastAPI()

# IMPORTANT: create MCP instance globally
mcp = FastAPIMCP(
    app,
    name="math-mcp-python",
)

# ---- Tools ----
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


# HEALTH CHECK (very important for Render)
@app.get("/")
def root():
    return {"status": "MCP server running"}