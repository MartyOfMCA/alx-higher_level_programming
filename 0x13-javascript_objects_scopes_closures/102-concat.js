#!/usr/bin/node
const fileSystem = require('fs').promises;

fileSystem.readFile(process.argv[2])
  .then(contents => fileSystem.writeFile(process.argv[4], contents))
  .catch(err => console.error(err));

fileSystem.readFile(process.argv[3])
  .then(contents => fileSystem.writeFile(process.argv[4],
    contents, { flag: 'a' }))
  .catch(err => console.error(err));
