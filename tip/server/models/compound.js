/**
 * TODO:
 *   1. check CID with PubChem (schema validation vs online validation)
 *   2. CAS: xxxxxxx-yy-z
 *       x: 2-7 digits, can leading digit be 0?
 *       y: can leading digit be 0?
 *   3. SMILES: rules?
 *   4. all validation after SMILES, rules?
 */

const Joi = require('joi');
const mongoose = require('mongoose');
const { schemaAssay } = require('./assay');

const Compound = mongoose.model('Compound', new mongoose.Schema({
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
  },
  assays: {
    type: [ mongoose.ObjectId ]
  },
  uploader: {
    type: String
  },
  upload_date: {
    type: Date,
    default: Date.now
  }
}));

function validate(data) {
  const schema = {
    count: Joi.number().integer().min(1),
    compounds: Joi.array().items(Joi.object().keys({
      cid: Joi.string().regex(/^[1-9]\d*$/),
      cas: Joi.string().regex(/^[1-9]\d{1,6}-\d{2}-\d/),  /* TODO */
      common_names: Joi.string().max(1000),
      iupac_name: Joi.string().max(1000),
      inchikey: Joi.string().regex(/^[A-Z]{14}-[A-Z]{10}-[A-Z]$/),
      smiles: Joi.string(),  /* TODO */
      mw: Joi.string(),
      comment: Joi.string().max(1000),
      assays: Joi.array().items(Joi.object().keys({
        protein: Joi.string(),
        gene: Joi.string(),
        ahr_type: Joi.string(),
        species: Joi.string(),
        conc_substrate: Joi.string(),
        conc_tested: Joi.string(),
        inhibition: Joi.string(),
        ec50: Joi.string(),
        pmid: Joi.string(),
        comment: Joi.string()
      }))
    })),
    uploader: Joi.string(),
  };

  return Joi.validate(data, schema);
}

// const options = { useUnifiedTopology: true };
// const url = 'mongodb://localhost:27017';
// const MongoClient = require('mongodb').MongoClient;

// async function insertDB(data) {

//   const client = await MongoClient.connect(url, options);
//   const db = await client.db('tipDB');
//   const assayCount = await db.collection('assays').countDocuments();
//   let curID = assayCount;
//   let insertingCompounds = [];
//   let insertingAssays = [];

//   // prepating inserting compounds and assays
//   for (let i = 0; i < data.compounds.length; i++) {
//     let compound = data.compounds[i];
//     let assays = compound.assays;
//     let assayIDs = [];

//     // relabelling assay IDs
//     for (let j = 0; j < assays.length; j++) {
//       assays[j]['compoundCID'] = compound.cid;
//       assays[j]['_id'] = curID;
//       insertingAssays.push(assays[j]);
//       assayIDs.push(curID);
//       curID += 1;
//     }

//     // checking and skipping existing compounds
//     let doc = await db.collection('compounds', options)
//               .find({ 'cid': compound.cid })
//               .toArray();
//     if (doc.length == 0) {
//       compound['assays'] = assayIDs;
//       insertingCompounds.push(compound);
//     }
//   }

//   // inserting
//   await db.collection('compounds').insertMany(insertingCompounds);
//   await db.collection('assays').insertMany(insertingAssays);
// }
// query

// update

// delete

module.exports.Compound = Compound;
module.exports.validateCompound = validate;
