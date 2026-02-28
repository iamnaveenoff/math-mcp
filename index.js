const express = require('express');
const app = express();

app.use(express.json());

// simple math operation handler
app.post('/math', (req, res) => {
  const { operation, operands } = req.body;
  if (!operation || !Array.isArray(operands)) {
    return res.status(400).json({ error: 'invalid request payload' });
  }

  let result;
  try {
    switch (operation) {
      case 'add':
        result = operands.reduce((a, b) => a + b, 0);
        break;
      case 'subtract':
        result = operands.reduce((a, b) => a - b);
        break;
      case 'multiply':
        result = operands.reduce((a, b) => a * b, 1);
        break;
      case 'divide':
        result = operands.reduce((a, b) => a / b);
        break;
      default:
        return res.status(400).json({ error: 'unsupported operation' });
    }
  } catch (err) {
    return res.status(500).json({ error: 'calculation error' });
  }

  res.json({ result });
});

// health check
app.get('/health', (req, res) => res.send('ok'));

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`math-mcp listening on port ${port}`);
});
