#!/usr/bin/node

const { argv } = require('node:process');

if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  const x = parseInt(argv[2]);
  let sq = '';
  let i = 0;
  for (i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      sq = sq + 'X';
    }
    if (i < (x - 1)) {
      sq = sq + '\n';
    }
  }
  console.log(sq);
}
