#!/usr/bin/node
const size = parseInt(process.argv[2]);
let counter = 0;

if (isNaN(size)) {
  console.log('Missing size');
}

while (counter < size) {
  console.log('X'.repeat(size));
  counter++;
}
