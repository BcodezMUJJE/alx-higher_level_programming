#!/usr/bin/node
const SquareBase = require('./5-square.js');
module.exports = class Square extends SquareBase {
  charPrint (char) {
    if (!char) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write(char);
        }
        process.stdout.write('\n');
      }
    }
  }
};
