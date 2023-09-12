#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return (list.filter((search) => search === searchElement).length);
};
