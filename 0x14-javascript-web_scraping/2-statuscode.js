#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

if (!url) {
  console.error('Please provide a URL as the first argument.');
  process.exit(1);
}

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error making request:', error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
