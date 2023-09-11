#!/usr/bin/node

const arg1 = process.argv[2];
const size = parseInt(arg1);

if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    let squareLine = "";

    for (let j = 0; j < size; j++) {
      squareLine += "X";
    }

    console.log(squareLine);
  }
} else {
  console.log("Missing size");
}
