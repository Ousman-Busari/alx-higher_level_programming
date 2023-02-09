#!/usr/bin/node
// prints all characters of a Star Wars movie:

const request = require('request');
const film_url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';

const pagePeople = "https://swapi-api.alx-tools.com/api/people/";
// request(url, (error, response, body) => {
//   if (!error) {
//     const people = JSON.parse(body).results
//     characters.forEach((character) => {
//       request(url, (error, response, body) => {
//         if (!error) {
//           const characters = JSON.parse(body).characters;
//           console.log(JSON.parse(body).name);
//         }
//       });
//     });
//   }
// });


function printCharacters(pagePeople) {
  request(pagePeople, (error, response, body) => {
    if (!error) {
      const page = JSON.parse(body)
      const people = JSON.parse(body).results;
      people.forEach(person => {
        if (person.films.includes(film_url)) {
          console.log(person.name);
        }
      })
      // console.log(page.next)
      if (page.next) {
        printCharacters(page.next);
      }
    }
  })
}

printCharacters(pagePeople)