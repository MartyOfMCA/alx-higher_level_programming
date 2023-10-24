#!/usr/bin/node
/*
 * Print the title of a Star Wars movie matching
 * the given episode.
 *
 * The script accepts the episode number from
 * which to retrieve the Star Wars movie.
 */

const request = require('request');
const { argv } = require('process');

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
if (argv.length === 3) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    console.log(JSON.parse(body).title);
  });
}
