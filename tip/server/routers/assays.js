/**
 * TODO:
 */
const express = require('express');
const { Assay, schemaAssay } = require('../models/assay');

const router = express.Router();

router.put('/:id', async (req, res) => {
  const { value, error } = schemaAssay.validate(req.body);
  if (error) return res.status(400).send(error.details[0].message);

  const assay = await Assay.findByIdAndUpdate({ _id: req.params.id },
    { $set: value }, { new: true });
  if (!assay) return res.status(404).send('The assay with the given ID \
    does not exist.');
  res.status(200).send(assay);
});

module.exports = router;
