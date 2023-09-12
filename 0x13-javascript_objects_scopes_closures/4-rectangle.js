#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log('');
    }
  }
  rotate () {
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
