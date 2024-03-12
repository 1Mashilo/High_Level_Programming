#!/usr/bin/node

const arg = process.argv[2];
const size = parseInt(arg);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let row = 0; row < size; row++) {
    let line = '';

    for (let col = 0; col < size; col++) {
      line += 'X';
    }

    console.log(line);
  }
}
