/**
 * TODO:
 */
const express = require('express');
const { Assay, validate } = require('../models/assay');

const router = express.Router();

// query
// router.get('/', (req, res) => {
//     res.send('Hello world!');
// });

module.exports.assays = router;
