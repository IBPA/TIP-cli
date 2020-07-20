/**
 * TODO:
 *   1. More sophiscated reading mechanism.
 *   2. router.get returning database assigned value "__v", delete it.
 */

const express = require('express');
const mongoose = require('mongoose');
const { Compound, validateCompound } = require('../models/compound');
const { Assay, createAssay, validateAssay} = require('../models/assay');

const router = express.Router();

router.post('/', async (req, res) => {
  const { error } = validateCompound(req.body);
  if (error) return res.status(400).send(error.details[0].message);

  for (let i = 0; i < req.body.compounds.length; i++) {
    let compound = req.body.compounds[i];
    let assays = compound.assays;
    let assayIds = [];

    for (let j = 0; j < assays.length; j++) {
      let objectID = await createAssay(assays[j]);

      assayIds.push(objectID);
      console.log(objectID);
    }
    compound.common_names = compound.common_names.split(';');
    compound.assays = assayIds;

    await new Compound(compound).save();
  }
  res.status(200).send(`Added ${req.body.compounds.length} documents.`);
});

router.get('/:name', async (req, res) => {
  // Finding by name (common names or IUPAC name).
  const courses = await Compound
    .find()
    .or([{ common_names: req.params.name }, { iupac_name: req.params.name }]);
  res.status(200).send(courses);
});

module.exports = router;
