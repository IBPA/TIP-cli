/**
 * TODO:
 */
const express = require('express');
const { Assay, validateAssay } = require('../models/assay');

const router = express.Router();

router.put('/:id', async (req, res) => {
  const { error } = validateAssay(req.body);
  if (error) return res.status(400).send(error.details[0].message);

  const assay = await Assay.findByIdAndUpdate({ _id: req.params.id },
    { $set: req.body }, { new: true });
  if (!assay) return res.status(404).send('The assay with the given ID \
    does not exist.');
  res.status(200).send(assay);
});

module.exports = router;
