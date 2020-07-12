// TODO
//  add comments, strying

const fs = require('fs');
const path = require('path');
const express = require('express');
const bodyParser = require('body-parser');

const port = process.env.PORT || 3000;
const app = express();
app.use(bodyParser.json());


// return schema
app.get('/api/schema', (req, res) => {
    const pathCompound = path.resolve(__dirname, "models/compound.txt");
    const pathAssay = path.resolve(__dirname, "models/assay.txt");
    const compoundHeader = fs.readFileSync(pathCompound, 'utf8');
    const assayHeader = fs.readFileSync(pathAssay, 'utf8');
    res.send({
        'compound' : compoundHeader,
        'assay' : assayHeader
    });
});

// upload
app.post('/api/upload', (req, res) => {
    res.send("Request received!");
    // insertDB(req.body);
    console.log(req.body);
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