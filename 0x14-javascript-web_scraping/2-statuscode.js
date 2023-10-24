#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

if (!url) {
  console.log('Usage: node 2-statuscode.js <URL>');
  process.exit(1);
}

request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
