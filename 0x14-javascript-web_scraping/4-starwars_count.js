#!/usr/bin/node
// Print number of movies where "Wedge Antilles" is present
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  let count = 0;
  const movie = JSON.parse(body).results;
  for (let i = 0; i < movie.length; i++) {
    if (JSON.stringify(movie[i].characters).match('18')) {
      count += 1;
    }
  }
  console.log(count);
});
