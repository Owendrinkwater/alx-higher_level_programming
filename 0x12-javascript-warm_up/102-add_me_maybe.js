#!/usr/bin/node

function addMeMaybe (number, theFunction) {
  number++; // increment number by 1
  theFunction(number); // call the given function with the new number
}

module.exports = { addMeMaybe };
