#!/usr/bin/node

const { argv } = require('node:process');

const len = argv.length;
if (len <= 3) {
  console.log(0);
} else {
  const numbers = [];
  for (let i = 2; i < len; i++) {
    numbers.push(parseInt(argv[i]));
  }
  numbers.sort(function (a, b) { return a - b; });
  numbers.reverse();
  console.log(numbers[1]);
}
