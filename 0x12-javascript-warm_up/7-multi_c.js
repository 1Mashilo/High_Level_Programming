#!/usr/bin/node

const arg = process.argv[2];

if (!isNaN(parseInt(arg))) {
  const x = parseInt(arg);
  let counter = 0;
  while (counter < x) {
    console.log('C is fun');
    counter++;
  }
} else {
  console.log('Missing number of occurrences');
}
