#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined || w < 1 || h < 1) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let counter = 0;
    for (counter = 0; counter < this.height; counter++) {
      console.log('X'.repeat(this.width));
    }
  }
};
