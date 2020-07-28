/**
 * TODO
 *   1. Elaborate schema.
 */
const Joi = require('joi');
const mongoose = require('mongoose');

/* TODO */
const schema = new mongoose.Schema({
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
})

const Assay = mongoose.model('Assay', schema);

async function createAssay(assay) {
  // Convert PMID string to an array.
  assay.pmid = assay.pmid.split(';');
  assayObject = await new Assay(assay).save();
  return assayObject._id;
}

/* TODO */
function validate(assay) {
  const schema = {
    protein: Joi.string(),
    gene: Joi.string(),
    ahr_type: Joi.string(),
    species: Joi.string(),
    conc_subtrate: Joi.string(),
    conc_tested: Joi.string(),
    inhibition: Joi.string(),
    ec50: Joi.string(),
    pmid: Joi.string(),
    comment: Joi.string()
  };

  return Joi.validate(assay, schema);
}

module.exports.Assay = Assay;
module.exports.schemaAssay = schema;
module.exports.createAssay = createAssay;
module.exports.validateAssay = validate;
