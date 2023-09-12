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

  rotate () {
    const tempWidth = this.width;
    this.width = this.height;
    this.height = tempWidth;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
