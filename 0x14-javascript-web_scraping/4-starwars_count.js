#!/usr/bin/node
/*
 * Print the number ogf movies where a named
 * character (Wedge Antilles) is presemt.
 *
 * The script accepts the Star Wars API URL
 * https://swapi-api.alx-tools.com/api/films/.
 */

const { argv } = require('process');
const request = require('request');

let numOfMovies = 0;

if (argv.length === 3) {
  request(argv[2], (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    JSON.parse(body).results.forEach(result => {
      result.characters.forEach(character => {
        if (character.includes(18)) {
          numOfMovies++;
        }
      });
    });

    console.log(numOfMovies);
  });
}
