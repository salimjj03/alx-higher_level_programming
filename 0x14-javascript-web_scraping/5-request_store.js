#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request.get(process.argv[2], (error, response, body) => {
  if (!error) {
    fs.writeFile(process.argv[3], body, 'utf-8', err => {
      if (err) console.log(err);
    }
    );
  }
});
