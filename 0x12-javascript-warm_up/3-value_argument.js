#!/usr/bin/node
const args = process.argv;
const argsCount = args.length;
console.log(argsCount === 2
  ? 'No argument'
  : args[2]);
