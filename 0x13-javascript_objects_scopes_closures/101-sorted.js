#!/usr/bin/node
const dict = require('./101-data').dict;
const userIDs = Object.values(dict);
const set = new Set(userIDs);
const setAsList = Array.from(set);
const entriesAsList = Object.entries(dict);
const newDict = {};
let occurences = [];

setAsList.forEach((id) => {
  occurences = [];
  entriesAsList.forEach((item) => {
    if (item[1] === id) {
      occurences.push(item[0]);
    }
  });
  newDict[id] = occurences;
});
console.log(newDict);
