#!/usr/bin/node
// Write a string to file
const r = require('fs');
const file = process.argv[2];
const s = process.argv[3];
r.writeFile(file, s, 'utf-8', function (err) {
  if (err) {
    return console.log(err);
  }
});
