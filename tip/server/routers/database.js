const fs = require('fs');
const path = require('path');
const express = require('express');

const router = express.Router();

router.get('/header', (req, res) => {
  const pathCompound = path.resolve(__dirname, "../templates/compound.txt");
  const pathAssay = path.resolve(__dirname, "../templates/assay.txt");
  const compoundHeader = fs.readFileSync(pathCompound, 'utf8');
  const assayHeader = fs.readFileSync(pathAssay, 'utf8');
  res.send({
    'compound' : compoundHeader,
    'assay' : assayHeader
  });
});

module.exports = router;
