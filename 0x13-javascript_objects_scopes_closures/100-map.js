#!/usr/bin/node
const arr = require('./100-data.js').list;
const newArray = arr.map(i => i * arr.indexOf(i));
console.log(arr);
console.log(newArray);
