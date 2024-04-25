#!/usr/bin/node


const fs = require('fs');
const filePath = process.argv[2];
const contentToWrite = process.argv[3];


if (!filePath || !contentToWrite) {
  console.error('Please provide both a file path and content to write as arguments.');
  process.exit(1);
}

fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
  if (err) {
    console.error('Error writing file:', err);
  }
});
