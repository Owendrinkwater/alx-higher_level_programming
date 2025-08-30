#!/usr/bin/node

function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction(); // call the function passed in
  }
}

module.exports = { callMeMoby };
