const express = require('express');
const bodyParser = require('body-parser');

const port = process.env.PORT || 3000;
const app = express();
app.use(bodyParser.json());

// upload
app.post('/api/upload', (req, res) => {
    res.send("Request received!");
    insertDB(req.body);
});

// query
// app.get('/', (req, res) => {
//     res.send('Hello world!');
// });

// app.get('/api/get/:id', (req, res) => {
    // req.params.id
// });

// // update
// app.put()

// // delete
// app.delete()

app.listen(port, () => console.log(`Listening on port ${port}...`));