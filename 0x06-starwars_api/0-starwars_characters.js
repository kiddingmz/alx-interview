#!/usr/bin/node

const request = require('request');
const FILMID = process.argv[2];

const URL_BASE = 'https://swapi-api.alx-tools.com/api/films';

function doRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, res, body) {
      if (!error && res.statusCode === 200) {
        resolve(JSON.parse(body));
      } else {
        reject(error);
      }
    });
  });
}

// Usage:

async function main (filmID) {
  const res = await doRequest(`${URL_BASE}/${filmID}`);
  for (const e of res.characters) {
    const pj = await doRequest(e);
    console.log(pj.name);
  }
}

main(FILMID);
