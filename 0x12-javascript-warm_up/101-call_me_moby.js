#!/usr/bin/node
// Execute function x times
exports.callMeMoby = function (x, func) {
  let i = 0;
  while (i < x) {
    func();
    i++;
  }
};
