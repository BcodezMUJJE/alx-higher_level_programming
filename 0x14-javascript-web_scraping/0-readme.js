#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];

if (!filePath) {
  console.log('Usage: node 0-readme.js <file_path>');
  process.exit(1);
}

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
