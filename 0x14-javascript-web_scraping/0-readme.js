#!/usr/bin/node
/*
 * Read the contents of a file provided as an
 * argument and print it's contents to the
 * standard output stream.
 *
 * The script accepts the file (relative path)
 * to read.
 */

const { argv } = require('process');
const { readFile } = require('fs');

if (argv.length === 3) {
  readFile(argv[2], 'utf8', (error, data) => {
    if (error) {
      console.error(error);
      return;
    }
    console.log(data);
  });
}
