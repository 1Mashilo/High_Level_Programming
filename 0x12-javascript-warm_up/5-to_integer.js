#!/usr/bin/node

const arg = process.argv[2];

const potentialNumber = Math.floor(Number(arg));

if (isNaN(potentialNumber)) {
  console.log('Not a number');
} else {
  console.log('My number:', potentialNumber);
}
