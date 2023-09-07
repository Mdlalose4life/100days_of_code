const express = require('express')
const app = express();

const server = app.listen(5000, () => {
    console.log('Server is running on port', server.address().port);
});

app.use(express.static(__dirname));