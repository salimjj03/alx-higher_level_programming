#!/usr/bin/node
const d = {};
const dict = require('./101-data.js').dict;
for (const key in dict) {
  const k = dict[key];
  if (d[k] === undefined) {
    d[k] = [key];
  } else {
    d[k].push(key);
  }
}
console.log(d);
