/**
 * TODO:
 *   1. More sophiscated reading mechanism.
 *   2. router.get returning database assigned value "__v", delete it.
 */

const express = require('express');
const mongoose = require('mongoose');
const { Compound, validateCompound } = require('../models/compound');
const { Assay, createAssay } = require('../models/assay');

const router = express.Router();

router.post('/', async (req, res) => {
  const { error } = validateCompound(req.body);
  if (error) return res.status(400).send(error.details[0].message);

  for (let i = 0; i < req.body.compounds.length; i++) {
    let compound = req.body.compounds[i];

    /* Check if this compound already exists in the database. */
    let existing = await Compound
      .find()
      .or([{ cid: Number(compound.cid) }, { cas: Number(compound.cas) }]);

    let assays = compound.assays;
    let assayIds = [];

    /* Create assay data and get reference Ids. */
    for (let j = 0; j < assays.length; j++) {
      assayIds.push(await createAssay(res, assays[j]));
    }

    if (!existing.length) {
      /* Parse string data and prepare to store in the database. */
      compound.assays = assayIds;
      compound.common_names = compound.common_names.split(';');
      await new Compound(compound).save();
    } else if (existing.length == 1) {
      existing[0].assays = existing[0].assays.concat(assayIds);
      await existing[0].save();
    } else {
      return res.status(500).send(`Server Error: Database debug needed.`)
    }
  }
  return res.status(200).send(`Added ${req.body.compounds.length} documents.`);
});

router.get('/:name', async (req, res) => {
  // Finding by name (common names or IUPAC name).
  const courses = await Compound
    .find()
    .or([{ common_names: req.params.name }, { iupac_name: req.params.name }]);
  res.status(200).send(courses);
});

// router.put('/:id', async (req, res) => {
//   const { error } = validateCompound(req.body);
//   if (error) return res.status(400).send(error.details[0].message);

//   const compound = await Compound
//     .findByIdAndUpdate(req.params.id, {

//     })
// });

module.exports = router;
