/**
 * [Joi description]
 * @type {[type]}
 */
const Joi = require('joi');
const { schemaCompound } = require('./compound');

const schema = Joi.object({
    count: Joi.number().integer().min(1),
    compounds: Joi.array().items(schemaCompound)
});

module.exports.schemaData = schema;
