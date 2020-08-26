/**
 * TODO:
 *   1. More sophiscated reading mechanism.
 *   2. create find existing compound is only checking cid and cas for now.
 *   3. create assign id bug: should not doc += 1
 */

const express = require('express');
const mongoose = require('mongoose');
const { schemaData } = require('../models/data');
const { Compound, schemaCompound } = require('../models/compound');
const { Assay, createAssays, deleteAssays } = require('../models/assay');

const router = express.Router();

router.post('/', async (req, res) => {
    const { value, error } = schemaData.validate(req.body);
    if (error) return res.status(400).send(error.details[0].message);

    const lastCompound = await Compound.findOne().sort('-_id').exec();
    const lastAssay = await Assay.findOne().sort('-_id').exec();
    let curCompoundID = (lastCompound !== null) ? lastCompound._id + 1 : 1;
    let curAssayID = (lastAssay !== null) ? lastAssay._id + 1 : 1;
    for (let i = 0; i < value.compounds.length; i++) {
        let compound = value.compounds[i];
        let assays = compound.assays;

        /* Check if this compound already exists in the database. */
        let found = await Compound.find()
            .or([{ cid: Number(compound.cid) },
                { cas: Number(compound.cas) }]);
        if (!found.length) {
            /* Create new compound document. */
            compound._id = curCompoundID++;
            curAssayID = await createAssays(res, assays, curAssayID,
                compound._id);
            await new Compound(compound).save();
        } else if (found.length == 1) {
            /* Compound existing, do not create a new compound. */
            curAssayID = await createAssays(res, assays, curAssayID,
                found[0]._id);
        } else {
            return res.status(500).send(
                `Server Error: Database debug needed.`);
        }
    }
    return res.status(200).send(
        `Added ${req.body.compounds.length} documents.`);
});

router.get('/', async (req, res) => {
    const compounds = await Compound.find(req.query);
    res.status(200).send(compounds);
});

router.put('/:id', async (req, res) => {
    const { value, error } = schemaCompound.validate(req.body);
    if (error) return res.status(400).send(error.details[0].message);

    const compound = await Compound.findByIdAndUpdate(
        req.params.id,
        { $set: value },
        { new: true });
    if (!compound) return res.status(404).send(
        'The compound with the given ID does not exist.');
    res.status(200).send(compound);
});


router.delete('/:id', async (req, res) => {
    const compound = await Compound.findByIdAndRemove(req.params.id);
    if (!compound) return res.status(404).send(
        'The compound with the given ID does not exist.');

    const assayLength = await deleteAssays(compound._id);
    res.status(200).send(compound);
});

module.exports = router;
