/**
 * TODO
 *   1. set config
 *   2. set logging
 */
const express = require('express');
const mongoose = require('mongoose');
const database = require('./routers/database');
const compounds = require('./routers/compounds');

const port = process.env.PORT || 3000;
const app = express();
const mongooseOptions = { useNewUrlParser: true, useUnifiedTopology: true };

mongoose.connect('mongodb://localhost/tip', mongooseOptions)
  .then(() => console.log('Connected to MongoDB...'))
  .catch(err => console.log('Could not connect to MongoDN...'))
app.use(express.json());
app.use('/compound', compounds);
app.use('/database', database);
app.listen(port, () => console.log(`Listening on port ${port}...`));
