/**
 * TODO
 *   1. set config
 *   2. set logging
 */
const express = require('express');
const mongoose = require('mongoose');
const database = require('./routers/database');
const compounds = require('./routers/compounds');

const port = process.env.PORT || 8001;
const app = express();
const mongooseOptions = { useNewUrlParser: true, useUnifiedTopology: true };
const url = 'mongodb+srv://admin:taglab@tip135@cluster0.fpktr.mongodb.net/tip?retryWrites=true&w=majority'

mongoose.connect(url, mongooseOptions)
  .then(() => console.log('Connected to MongoDB...'))
  .catch(err => console.log(err))
app.use(express.json());
app.use('/compound', compounds);
app.use('/database', database);
app.listen(port, () => console.log(`Listening on port ${port}...`));
