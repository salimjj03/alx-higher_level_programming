#!/usr/bin/node
if (!isNaN(process.argv[2])) {
  for (let i = 0; i < process.argv[2]; i++) {
    let line = '';
    for (let j = 0; j < process.argv[2]; j++) {
      line += '#';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
