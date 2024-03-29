#!/usr/bin/node
// prints the number of movies where the character "Wedge Antilles" is present

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, episode) => {
      return episode.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
