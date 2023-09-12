#!/usr/bin/node

const OldSquare = require('./5-square');

module.exports = class Square extends OldSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let counter = 0;
    for (counter = 0; counter < this.height; counter++) {
      if (c === undefined) {
        c = 'X';
      }
      console.log(c.repeat(this.width));
    }
  }
};
