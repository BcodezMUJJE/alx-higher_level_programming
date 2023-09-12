#!/usr/bin/node
const { dict } = require('./101-data.js');
const computed = Object.entries(dict).reduce((prev, val) => {
  prev[val[1]] = prev[val[1]]?.concat(val[0]) || [val[0]];
  return prev;
}, {});
console.log(computed);
