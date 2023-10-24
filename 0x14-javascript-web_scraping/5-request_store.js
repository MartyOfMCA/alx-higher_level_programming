#!/usr/bin/node
/*
 * Retrieve the contents of a webpage and store
 * the retrieved contents to a file.
 *
 * The script takes the URL to crawl as an
 * argument and the relative path to store the
 * file respectively.
 */

const { writeFile } = require('fs');
const { argv } = require('process');
const request = require('request');

if (argv.length === 4) {
  request(argv[2], (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    writeFile(argv[3], body, (error) => {
      if (error) {
        console.error(error);
      }
    });
  });
}
