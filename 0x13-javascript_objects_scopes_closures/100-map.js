#!/usr/bin/node
const arr = require('./100-data.js').list;
const newArray = arr.map((i, index) => i * index);
console.log(arr);
console.log(newArray);
