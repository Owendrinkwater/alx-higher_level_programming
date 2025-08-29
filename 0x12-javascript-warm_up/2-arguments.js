#!/usr/bin/node
// Script that prints a message depending on number of arguments

const args = process.argv.length - 2;

if (args === 0) {
  console.log('No argument');
} else if (args === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
