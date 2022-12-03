// read the file
function print(x) {
    return console.log(x);
}

function sum(a, b) {
    return a+b;
}

let fs = require('fs');

// let data = fs.readFileSync("./sample_input.txt", "utf-8");
let data = fs.readFileSync("./input.txt", "utf-8");

// remove the trailing newline
data = data.trim();

// split on empty line
var elfCalories = data.split("\n\n");

elfCalories = elfCalories.map((x) => x.split("\n"));

// convert each array into a float array and find the max
for (var i=0; i<elfCalories.length; i++) {
    // convert the string list into a float list
    // elfCalories[i] = elfCalories[i].map((x) => parseFloat(x)) 
    elfCalories[i] = new Float32Array(elfCalories[i])
    // elfCalories[i] = elfCalories[i].map(Number);
    // elfCalories[i] = elfCalories[i].reduce((previous, current) => {
    //     return previous + current
    // }, 0)
    elfCalories[i] = elfCalories[i].reduce(sum, 0)
}

// get the max of the elfCalories
elfCalories = new Float32Array(elfCalories)
print(Math.max(...elfCalories))

// Part 2 begins
// sort the elfCalories and find the sum of the top 3
elfCalories.sort()
print(elfCalories.slice(-3).reduce(sum, 0))
