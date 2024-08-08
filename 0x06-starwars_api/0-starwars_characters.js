#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

request(
  `https://swapi-api.alx-tools.com/api/films/${movieId}/`,
  async (error, response, body) => {
    if (error) {
      console.log(error);
    }
    const characters = JSON.parse(body).characters;
    for (const characterUrl of characters) {
      await new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            console.log(JSON.parse(body).name);
            resolve();
          }
        });
      });
    }
  }
);
