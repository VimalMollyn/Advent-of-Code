## Day 3

Did the part one with a kind of interesting observation that number ranges fully intersect if the product of the differences of the 2 ranges is 0 or negative. For part 2, I gave chatGPT the following prompt:

"Given an input string as follows:

"2-4,6-8"

write a js script that tells me if these number ranges intersect"

And it gave me the following code:

```
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

// Test the function
console.log(rangesIntersect("2-4,6-8")); // Output: false
console.log(rangesIntersect("2-6,4-8")); // Output: true
console.log(rangesIntersect("2-8,4-6")); // Output: true
console.log(rangesIntersect("2-3,4-5")); // Output: false
```
I am blown away. 
