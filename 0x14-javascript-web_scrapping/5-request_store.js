#!/usr/bin/node
// gets the content of a webpagae and stores it in a file

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const fileName = process.argv[3];
request(url).pipe(fs.createWriteStream(fileName));
