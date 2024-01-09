#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let o = 0;
  for (const i of list) {
    if (i === searchElement) {
      o += 1;
    }
  }
  return (o);
};
