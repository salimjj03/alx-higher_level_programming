#!/usr/bin/node
exports.esrever = function (list) {
  const ls = [];
  const len = list.length - 1;
  for (let i = len; i >= 0; i--) {
    ls.push(list[i]);
  }
  return (ls);
};
