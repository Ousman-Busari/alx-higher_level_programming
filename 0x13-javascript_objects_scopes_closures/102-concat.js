#!/usr/bin/node
const editor = require('fs');
const fileA = editor.readFileSync(process.argv[2]);
const fileB = editor.readFileSync(process.argv[3]);
editor.writeFileSync(process.argv[4], fileA + fileB);
