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
    _id: {
        type: Number
    },
    compound: {
        type: Number
    },
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
    },
    uploader: {  // required in the future
        type: String
    },
    upload_date: {
        type: Date,
        default: Date.now
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

async function createAssays(assays, assayIdStart, compoundId) {
    for (let i = 0; i < assays.length; i++) {
        assays[i]._id = assayIdStart++;
        assays[i].compound = compoundId;
        await new Assay(assays[i]).save();
    }
    return assayIdStart;
}

async function deleteAssays(compoundId) {
    const assays = await Assay.find({ compound: compoundId });
    assays.forEach(async assay => {
        await Assay.findByIdAndRemove(assay._id);
    })
    return assays.length;
}

module.exports.Assay = Assay;
module.exports.schemaAssay = schema;
module.exports.createAssays = createAssays;
module.exports.deleteAssays = deleteAssays;
