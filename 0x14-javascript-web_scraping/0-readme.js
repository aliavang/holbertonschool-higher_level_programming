#!/usr/bin/node
// Read and print content of file
const r = require('fs');
const file = process.argv[2];
r.readFile(file, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  }
  console.log(String(data).replace('\n', ''));
});
