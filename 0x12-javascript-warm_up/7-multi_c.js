#!/usr/bin/node
// Print string x times
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < parseInt(process.argv[2])) {
    console.log('C is fun');
    i++;
  }
}
