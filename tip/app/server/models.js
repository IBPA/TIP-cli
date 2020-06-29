const MongoClient = require('mongodb').MongoClient;

const url = 'mongodb://localhost:27017';
const options = { useUnifiedTopology: true };

// insert
async function insertDB(data) {

    const client = await MongoClient.connect(url, options);
    const db = await client.db('tipDB');
    const assayCount = await db.collection('assays').countDocuments();
    let curID = assayCount;
    let insertingCompounds = [];
    let insertingAssays = [];

    // prepating inserting compounds and assays
    for (let i = 0; i < data.compounds.length; i++) {
        let compound = data.compounds[i];
        let assays = compound.assays;
        let assayIDs = [];

        // relabelling assay IDs
        for (let j = 0; j < assays.length; j++) {
            assays[j]['compoundCID'] = compound.cid;
            assays[j]['_id'] = curID;
            insertingAssays.push(assays[j]);
            assayIDs.push(curID);
            curID += 1;
        }

        // checking and skipping existing compounds
        let doc = await db.collection('compounds', options)
                .find({ 'cid': compound.cid })
                .toArray();
        if (doc.length == 0) {
            compound['assays'] = assayIDs;
            insertingCompounds.push(compound);
        }
    }

    // inserting
    await db.collection('compounds').insertMany(insertingCompounds);
    await db.collection('assays').insertMany(insertingAssays);
}
// query

// update

// delete

exports.insertDB = insertDB;