#!/usr/bin/node
// Display status code of GET request
const request = require('request');
request(process.argv[2], function (error, response) {
  if (error) {
    console.log(error);
  }
  console.log('code: ' + response.statusCode);
});
