#!/usr/bin/node
// prints the title of a Star Wars movie where
// the episode matches a given number

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  console.log(error || JSON.parse(body).title);
});
