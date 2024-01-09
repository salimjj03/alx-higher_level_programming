#!/usr/bin/node
module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.width; i++) console.log(c.repeat(this.width));
    } else if (c === undefined) {
      this.print();
    }
  }
};
