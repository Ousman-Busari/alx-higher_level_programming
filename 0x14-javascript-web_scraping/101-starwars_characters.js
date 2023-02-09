#!/usr/bin/node
// prints all characters of a Star Wars movie:

const request = require('request');
const filmURL = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';
const pagePeople = 'https://swapi-api.alx-tools.com/api/people/';

function printCharacters (pagePeople) {
  request(pagePeople, (error, response, body) => {
    if (!error) {
      const page = JSON.parse(body);
      const people = JSON.parse(body).results;
      people.forEach(person => {
        if (person.films.includes(filmURL)) {
          console.log(person.name);
        }
      });
      if (page.next) {
        printCharacters(page.next);
      }
    }
  });
}

printCharacters(pagePeople);
