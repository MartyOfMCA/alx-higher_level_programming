#!/usr/bin/node
/*
 * Compute the number of tasks completed by users
 * by their ID.
 *
 * The script takes the API URL to be used for the
 * request as the argumen.
 * https://jsonplaceholder.typicode.com/todos
 */

const { argv } = require('process');
const request = require('request');
const obj = {};

if (argv.length === 3) {
  request(argv[2], (error, response, body) => {
    if (error) {
      console.error(error);
    }

    JSON.parse(body).forEach(result => {
      if (result.completed) {
        obj[result.userId] = (obj[result.userId] === undefined) ? 1 : obj[result.userId] += 1;
      }
    });

    console.log(obj);
  });
}
