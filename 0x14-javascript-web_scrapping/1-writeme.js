#!/usr/bin/node
// writes a string to a file

const { writeFile } = require('fs');

const filePath = process.argv[2];
const fileContent = process.argv[3];

writeFile(filePath, fileContent, err => {
  if (err) console.log(err);
}
);
