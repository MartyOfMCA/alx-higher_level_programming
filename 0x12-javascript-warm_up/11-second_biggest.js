#!/usr/bin/node
let numbers = process.argv.splice(2);

if (numbers.length < 2) {
  console.log(0);
} else {
  numbers = numbers.sort(naturalSort).reverse();
  console.log(numbers[1]);
}

function naturalSort (num1, num2) {
  return (num1 - num2);
}
