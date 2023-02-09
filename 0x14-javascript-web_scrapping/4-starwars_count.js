#!/usr/bin/node
// prints the number of movies where the character "Wedge Antilles" is present

const request = require('request');

const url = process.argv[2];
// Wedge Antilles uri
const uri = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (error, response, body) => {
  console.log(error || JSON.parse(body)
    .results
    .map((episode) => episode.characters)
    .filter((episodeCharacters) => episodeCharacters.includes(uri))
    .length);
});
