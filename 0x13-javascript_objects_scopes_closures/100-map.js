#!/usr/bin/node
const { list } = require('./100-data.js');
const computedList = list.map((v, idx) => v * idx);
console.log(list);
console.log(computedList);
