#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length <= 2) {
  console.log('Usage: node script.js <film-id>');
  process.exit(1);
}

const filmId = process.argv[2];
const filmUrl = `${API_URL}/films/${filmId}/`;

request.get(filmUrl, (err, response, body) => {
  if (err || response.statusCode !== 200) {
    console.error('Error:', err || body);
    process.exit(1);
  }

  const characters = JSON.parse(body).characters;
  const promises = characters.map((url) => {
    return new Promise((resolve, reject) => {
      request.get(url, (err, response, body) => {
        if (err || response.statusCode !== 200) {
          reject(err || body);
        } else {
          const characterName = JSON.parse(body).name;
          resolve(characterName);
        }
      });
    });
  });

  Promise.all(promises)
    .then((names) => {
      console.log(names.join('\n'));
    })
    .catch((err) => {
      console.error('Error:', err);
      process.exit(1);
    });
});
