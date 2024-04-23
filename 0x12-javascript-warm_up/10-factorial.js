#!/usr/bin/node

const { argv } = require('node:process');

function factorial (a) {
  if (a === 0) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

let number;
if (isNaN(argv[2])) {
  number = 0;
} else {
  number = parseInt(argv[2]);
}

console.log(factorial(number));
