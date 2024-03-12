#!/usr/bin/node

const arg = process.argv[2];

const converted = parseInt(arg); 

if (isNaN(converted)) {
    console.log("Not a number");
} else {
    console.log("My Number:", converted);
}

