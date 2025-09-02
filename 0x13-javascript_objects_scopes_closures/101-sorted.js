#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};

for (const userId in dict) {
  const occur = dict[userId];

  if (!newDict[occur]) {
    newDict[occur] = [];
  }
  newDict[occur].push(userId);
}

console.log(newDict);
