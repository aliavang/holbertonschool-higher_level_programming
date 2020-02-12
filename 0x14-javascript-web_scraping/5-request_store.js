#!/usr/bin/node
// Get content of webpage and store in file
const request = require('request');
const r = require('fs');
const file = process.argv[3];
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  r.writeFile(file, body, 'utf-8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
