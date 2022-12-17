function print(x) {
    return console.log(x);
}

let fs = require('fs');

// let data = fs.readFileSync("./sample_input.txt", "utf-8");
let data = fs.readFileSync("./input.txt", "utf-8");

// remove the trailing newline
data = data.trim();

var assignment_pairs = data.split("\n")
var total_overlap = 0;
for (let i=0;i<assignment_pairs.length; i++) {
    let assignments = assignment_pairs[i].split(",");
    // print(assignments);
    let assignment1 = assignments[0].split("-").map((x) => parseInt(x));
    let assignment2 = assignments[1].split("-").map((x) => parseInt(x));

    let prod = 1;
    for (let j=0; j<assignment1.length; j++) {
        prod *= assignment1[j] - assignment2[j];
        // diff.push();
    }
    // print(prod);
    total_overlap += (prod <= 0) ? 1 : 0;
}
print(total_overlap);

// part 2
function rangesIntersect(input) {
  // Split the input string into an array of ranges
  let ranges = input.split(',');

  // Split each range into an array of numbers
  let range1 = ranges[0].split('-').map(Number);
  let range2 = ranges[1].split('-').map(Number);

  // Check if the ranges intersect
  if (range1[0] <= range2[1] && range2[0] <= range1[1]) {
    return true;
  } else {
    return false;
  }
}
var total_partial_overlap = 0;
var total_intersect = 0;
for (let i=0;i<assignment_pairs.length; i++) {
    let prod = rangesIntersect(assignment_pairs[i]);
    total_intersect += (prod) ? 1 : 0;
}
print(total_intersect);
