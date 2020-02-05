#!/usr/bin/node
// Add two integers
function add (a, b) {
  console.log(a + b);
}

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('NaN');
} else if (isNaN(process.argv[3]) || process.argv[3] === undefined) {
  console.log('NaN');
} else if (process.argv.length < 3) {
  console.log('NaN');
} else {
  add(parseInt(process.argv[2]), parseInt(process.argv[3]));
}
