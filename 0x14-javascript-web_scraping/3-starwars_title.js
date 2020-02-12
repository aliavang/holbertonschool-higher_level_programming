#!/usr/bin/node
// Print title of Star Wars movie if given number matches episode number
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const movie = JSON.parse(body).title;
  console.log(movie);
});
