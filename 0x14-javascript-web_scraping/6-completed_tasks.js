#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (!error) {
    const dos = JSON.parse(body);
    const complete = {};
    dos.forEach((tdo) => {
      if (tdo.completed && complete[tdo.userId] === undefined) {
        complete[tdo.userId] = 1;
      } else if (tdo.completed) {
        complete[tdo.userId] += 1;
      }
    });
    console.log(complete);
  }
});
