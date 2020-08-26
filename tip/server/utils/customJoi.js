/**
 * [Joi description]
 * @type {[type]}
 */
const Joi = require('joi');

const CustomJoi = Joi.extend((joi) => {

  return {
    type: 'stringArray',
    base: Joi.array(),
    coerce(value, helpers) {
      return { value: value.split(';') };
    }
  }
});

module.exports = CustomJoi;
