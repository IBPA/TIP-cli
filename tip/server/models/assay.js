/**
 * TODO
 *   1. Elaborate schema.
 *   2. what if duplicate assays?
 */
const Joi = require('joi');
const mongoose = require('mongoose');
const CustomJoi = require('../utils/customJoi');
const { integer, float } = require('../utils/regex');

const Assay = mongoose.model('Assay', new mongoose.Schema({
  protein: {
    type: String
  },
  gene: {
    type: String
  },
  ahr_type: {
    type: String,
    enum: ['LB', 'DB', 'GE']
  },
  species: {
    type: String
  },
  conc_subtrate: {
    type: Number
  },
  conc_tested: {
    type: Number
  },
  inhibition: {
    type: Number
  },
  ec50: {
    type: String
  },
  pmid: {
    type: [ Number ]
  },
  comment: {
    type: String,
    max: 1000
  }
}));

/* TODO */
const schema = Joi.object({
  protein: Joi.string(),
  gene: Joi.string(),
  ahr_type: Joi.string().valid('LB', 'DB', 'GE'),
  species: Joi.string(),  // TODO
  conc_substrate: Joi.string().regex(float),
  conc_tested: Joi.string().regex(float),
  inhibition: Joi.string().regex(float),
  ec50: Joi.string(),
  pmid: CustomJoi.stringArray().items(Joi.number()).prefs({ convert: true }),  // TODO
  comment: Joi.string().max(1000)
});

async function createAssay(res, assay) {
  const { error } = validate(assay);
  if (error) return res.status(400).send(error.details[0].message);

  /* Convert PMID string to an array. */
  // assay.pmid = assay.pmid.split(';');

  assayObject = await new Assay(assay).save();
  return assayObject._id;
}

module.exports.Assay = Assay;
module.exports.schemaAssay = schema;
module.exports.createAssay = createAssay;
