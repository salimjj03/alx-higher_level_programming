#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, (error, response, body) => {
  if (!error) {
    let count = 0;
    const ls = JSON.parse(body).results;
    for (const i in ls) {
      if (ls[i].characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) { count++; }
    }
    console.log(count);
  }
});
