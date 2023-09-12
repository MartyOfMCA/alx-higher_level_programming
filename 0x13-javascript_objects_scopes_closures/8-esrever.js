#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  let counter = list.length - 1;
  for (; counter >= 0; counter--) {
    newList.push(list[counter]);
  }
  return (newList);
};
