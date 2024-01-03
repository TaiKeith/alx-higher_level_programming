#!/usr/bin/node
const fs = require('fs')

if (process.argv.length !== 3) {
	console.error('Usage: ./script.js <file>');
	process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
	if (err) {
		console.error(err);
	} else {
		console.log(`${data}`);
	}
});
