const Joi = require('joi');
const { schemaCompound } = require('./compound');

function validate(data) {
  const schema = {
    count: Joi.number().integer().min(1),
    compounds: Joi.array().items(schemaCompound)
    // user: Joi.string().min(4),
    // pw: Joi.string()
  };
  return Joi.validate(data, schema);
}

module.exports.validateData = validate;
