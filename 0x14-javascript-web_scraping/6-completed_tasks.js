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
let results = [];
const obj = {};
let completedTasks = 0;
let userId = 1;
let counter = 1;

if (argv.length === 3) {
  request(argv[2], (error, response, body) => {
    if (error) {
      console.error(error);
    }

    results = JSON.parse(body);

    results.forEach(result => {
      counter = result.userId;

      if (counter !== userId) {
        if (completedTasks > 0) {
          obj[userId] = completedTasks;
        }
        userId = counter;
        completedTasks = 0;
      }

      if (result.completed) {
        completedTasks++;
      }
    });

    if (completedTasks > 0) {
      obj[userId] = completedTasks;
    }

    console.log(obj);
  });
}
