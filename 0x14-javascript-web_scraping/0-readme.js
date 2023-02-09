#!/usr/bin/node
// reads and prints the content of a file
const { readFileSync } = require('fs');

const file = process.argv[2];

try {
  console.log(readFileSync(file, 'utf8'));
} catch (error) {
  console.log(error);
}
