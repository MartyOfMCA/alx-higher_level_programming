#!/usr/bin/node
exports.converter = function (radix) {
  return function (number) {
    return number.toString(radix);
  };
};
