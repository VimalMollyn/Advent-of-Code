function print(x) {
    return console.log(x);
}

let fs = require('fs');

// let data = fs.readFileSync("./sample_input.txt", "utf-8");
let data = fs.readFileSync("./input.txt", "utf-8");

// remove the trailing newline
data = data.trim();

const priorities = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52
}

var rucksacks = data.split("\n")
var total_priority = 0;
for (let i=0;i<rucksacks.length; i++) {
    let rucksack = rucksacks[i];

    let comp_1 = rucksack.slice(0, Math.floor(rucksack.length/2));
    let comp_2 = rucksack.slice(Math.floor(rucksack.length/2));

    var comp_1_chars = new Set(comp_1.split(""));
    var comp_2_chars = new Set(comp_2.split(""));

    // get the differences between the two strings
    var intersection = [...comp_1_chars].filter(x => comp_2_chars.has(x));

    total_priority += priorities[intersection[0]];
}
print(total_priority);

// part two
// split input into chunks of 3 lines 
total_priority = 0;
for (let i = 0; i < rucksacks.length; i += 3) {
    var group = rucksacks.slice(i, i + 3);

    var set_1 = new Set(group[0].split(""));
    var set_2 = new Set(group[1].split(""));
    var set_3 = new Set(group[2].split(""));


    // get the differences between the two strings
    var intersection = [...set_1].filter(x => set_2.has(x) && set_3.has(x));
    total_priority += priorities[intersection[0]];
}

print(total_priority);
