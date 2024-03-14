#!usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0 && Number.isInteger(w)) && (h > 0 && Number.isInteger(h))) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object in case of invalid input
    }
  }
}

module.exports = Rectangle;
