#!/usr/bin/node
/*
 * Write the given string to the file provided as
 * arguments.
 *
 * The script accepts the file (relative path)
 * to read and the string to be written to the
 * file.
 */

const { argv } = require('process');
const { writeFile } = require('fs');

if (argv.length === 4) {
  writeFile(argv[2], argv[3], error => {
    if (error) {
      console.error(error);
    }
  });
}
