# math-mcp

A minimal Model Context Protocol (MCP) server implemented in Node.js that performs basic math operations. Designed to be deployed on Render or similar platforms.

## Endpoints

- `POST /math` - perform an operation
  - Request body: `{ "operation": "add|subtract|multiply|divide", "operands": [number, ...] }`
  - Response: `{ "result": number }`

- `GET /health` - simple health check returning `ok`

## Startup

```bash
npm install
npm start
```

## Deployment to Render

Render can build this service directly from the repo. It detects the `npm start` script and will set the `PORT` environment variable automatically.
Alternatively, use the supplied `Dockerfile` if you prefer a container deployment.
