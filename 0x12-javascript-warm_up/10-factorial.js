#!/usr/bin/node

function factorial(n) {
  if (isNaN(n) || n < 0) {
    // Factorial of NaN or negative number is not defined; return 1 as specified.
    return 1;
  } else if (n === 0) {
    // Base case: factorial of 0 is 1.
    return 1;
  } else {
    // Recursive case: Compute factorial by multiplying n with factorial(n-1).
    return n * factorial(n - 1);
  }
}

const arg1 = process.argv[2];
const integerArg = parseInt(arg1);

const result = factorial(integerArg);
console.log(result);

