#!/usr/bin/node
const fs = require('fs/promises');
const args = process.argv.slice(2);
fs.readFile(args[0], 'utf8').then((dataA) => {
  fs.readFile(args[1], 'utf8').then(dataB => {
    fs.writeFile(args[2], `${dataA}${dataB}`, (err) => console.error(err));
  });
});
