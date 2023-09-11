#!/usr/bin/node
const times = parseInt(process.argv[2]);
let counter = 0;

if (isNaN(times)) {
  console.log('Missing number of occurences');
}

for (counter = 0; counter < times; counter++) {
  console.log('C is fun');
}
