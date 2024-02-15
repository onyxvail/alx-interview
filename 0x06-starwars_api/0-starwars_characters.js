#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const starWarsAPI = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(starWarsAPI, function (error, res, body) {
  if (error) {
    console.log('Error', error);
  }
  const charactersURL = JSON.parse(body).characters;
  const size = charactersURL.length;
  const array = Array(size).fill();
  let count = 0;
  for (let i = 0; i < size; i++) {
    request(charactersURL[i], function (error, res, body) {
      if (error) {
        console.log(error);
      } else {
        array[i] = JSON.parse(body).name;
        count++;
      }
      if (count === size) {
        for (let j = 0; j < size; j++) {
          console.log(array[j]);
        }
      }
    });
  }
});
