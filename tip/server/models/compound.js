/**
 * TODO:
 *   1. check CID with PubChem (schema validation vs online validation)
 *   2. CAS: xxxxxxx-yy-z
 *       x: 2-7 digits, can leading digit be 0?
 *       y: can leading digit be 0?
 *   3. SMILES: rules?
 *   4. all validation after SMILES, rules?
 *   5. Check duplicate compounds that not in pubchem.
 */

const Joi = require('joi');
const mongoose = require('mongoose');
const CustomJoi = require('../utils/customJoi');
const { schemaAssay } = require('./assay');
const { integer, float } = require('../utils/regex');

const Compound = mongoose.model('Compound', new mongoose.Schema({
    _id: {
        type: Number
    },
    cid: {
        type: Number
    },
    cas: {
        type: String
    },
    common_names: {
        type: [ String ]
    },
    iupac_name: {
        type: String
    },
    inchikey: {
        type: String
    },
    smiles: {
        type: String
    },
    mw: {
        type: Number
    },
    comment: {
        type: String,
        max: 1000
    }
}));

const schema = Joi.object({
    cid: Joi.string().regex(integer),
    cas: Joi.string().regex(/^[1-9]\d{1,6}-\d{2}-\d$/),  /* TODO */
    common_names: CustomJoi.stringArray().items(Joi.string())
        .prefs({ convert: true }),
    iupac_name: Joi.string().max(1000),
    inchikey: Joi.string().regex(/^[A-Z]{14}-[A-Z]{10}-[A-Z]$/),
    smiles: Joi.string(),  /* TODO */
    mw: Joi.string().regex(float),
    comment: Joi.string().max(1000),
    assays: Joi.array().items(schemaAssay),
    });

module.exports.Compound = Compound;
module.exports.schemaCompound = schema;
