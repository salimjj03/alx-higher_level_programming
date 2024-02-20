#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const dos = JSON.parse(body);
    let complete = {};
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
