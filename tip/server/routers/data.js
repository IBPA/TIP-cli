/**
 * TODO:
 */
const express = require('express');
const { Data, validate } = require('../models/compound');

const router = express.Router();

// upload
router.post('/create', (req, res) => {
  const { error } = validate(req.body);
  if (error) return res.status(400).send(result.error.details[0].message);

  console.dir(JSON.stringify(req.body));

  // insertDB(req.body);
});

// query
// router.get('/', (req, res) => {
//     res.send('Hello world!');
// });

module.exports = router;
