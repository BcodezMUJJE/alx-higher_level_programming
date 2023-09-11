#!/usr/bin/node

const arg1 = process.argv[2];
const x = parseInt(arg1);

if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log("C is fun");
  }
} else {
  console.log("Missing number of occurrences");
}
