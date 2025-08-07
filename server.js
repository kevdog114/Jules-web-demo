const express = require('express');
const app = express();
const port = 3000;

app.get('/api/ip', (req, res) => {
  const ip = req.ip;
  res.json({ ip });
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
