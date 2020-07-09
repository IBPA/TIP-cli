// TODO
//  add comments, strying

const fs = require('fs');
const express = require('express');
const bodyParser = require('body-parser');

const port = process.env.PORT || 3000;
const app = express();
app.use(bodyParser.json());


// return schema
app.get('/api/schema', (req, res) => {
    const compoundHeader = fs.readFileSync('models/compound.txt', 'utf8');
    const assayHeader = fs.readFileSync('models/assay.txt', 'utf8');
    res.send({
        'compound' : compoundHeader,
        'assay' : assayHeader
    });
});

// upload
app.post('/api/upload', (req, res) => {
    res.send("Request received!");
    // insertDB(req.body);
    console.log(req.body)
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