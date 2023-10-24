#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3]

if (!filePath || !content) {
  console.log('Usage: node 1-writeme.js <file_path> <string_to_write>');
  process.exit(1);
}

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err); // Print the error object
  } else {
    console.log('File written successfully');
  }
});

