/**
 * A regex definition for integer.
 * @type {RegExp}
 */
const integer = /^[1-9]\d*$/;

/**
 * A regex definition for float.
 * @type {RegExp}
 */
const float = /^(?:0|[1-9]\d*)(?:\.\d{1,2})?$/;

module.exports.integer = integer;
module.exports.float = float;
