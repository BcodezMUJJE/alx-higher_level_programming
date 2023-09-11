#!/usr/bin/node

function add(a, b) {
  return a + b;
}
const arg1 = process.argv[2];
const arg2 = process.argv[3];

const int1 = parseInt(arg1);
const int2 = parseInt(arg2);

if (!isNaN(int1) && !isNaN(int2)) {
  const result = add(int1, int2);
  console.log(result);
} else {
  console.log("NaN");
}
