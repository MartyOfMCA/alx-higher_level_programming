#!/usr/bin/node
/*
 * Display the status code of a get request using
 * the request node module.
 *
 * The script accepts the URL to make the
 * request to.
 */
const request = require('request');
const { argv } = require('process');

if (argv.length === 3) {
  request(argv[2], (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    console.log(`code: ${response.statusCode}`);
  });
}
