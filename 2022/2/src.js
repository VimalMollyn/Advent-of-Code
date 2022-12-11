function print(x) {
    return console.log(x);
}

function sum(a, b) {
    return a+b;
}

const choice_value = {
    "X": 1,
    "Y": 2,
    "Z": 3
};

function get_score(opp_choice, your_choice) {
    var score = 0;
    score += choice_value[your_choice];

    if (opp_choice == "A") {
        if (your_choice == "X") {
            // draw
            score += 3;
            return score
        }
        else if (your_choice == "Z") {
            // rock beats scissors
            // lose
            score += 0;
            return score
        }
        else {
            // rock loses to paper
            // win 
            score += 6;
            return score
        }
    }
    else if (opp_choice == "C") {
        if (your_choice == "X") {
            // win
            score += 6;
            return score
        }
        else if (your_choice == "Z") {
            // draw
            score += 3;
            return score
        }
        else {
            // lose
            score += 0;
            return score
        }
    }
    else {
        // opp_choice == "C"
        if (your_choice == "X") {
            // lose
            score += 0;
            return score
        }
        else if (your_choice == "Z") {
            // win
            score += 6;
            return score
        }
        else {
            // draw
            score += 3;
            return score
        }
    }
}

const { resolve6 } = require('dns');
let fs = require('fs');

// let data = fs.readFileSync("./sample_input.txt", "utf-8");
let data = fs.readFileSync("./input.txt", "utf-8");

// remove the trailing newline
data = data.trim();

// split on empty line
// get a score for each line
var rounds = data.split("\n")
var total_score = 0;
for (let i=0;i<rounds.length; i++) {
    var choices = rounds[i].split(" ");
    var opp_choice = choices[0];
    var your_choice = choices[1];

    let score = get_score(opp_choice, your_choice);
    total_score += score;
}

print(total_score);

// part 2
// X -> lose
// Y -> draw
// Z -> win

const lose_choice = {
    "A": "Z", // rock wins to scissors
    "B": "X", // paper wins to rock
    "C": "Y" // scissors wins to paper 
};

const win_choice = {
    "A": "Y", // rock loses to paper
    "B": "Z", // paper loses to scissors
    "C": "X" // scissors loses to rock 
};

const draw_choice = {
    "A": "X", 
    "B": "Y", 
    "C": "Z" 
};

const strategy_score = {
    "X": 0,
    "Y": 3,
    "Z": 6 
};

function get_command(strategy, opp_choice) {
    if (strategy == "X") {
        // lose 
        return lose_choice[opp_choice];
    }
    else if (strategy == "Y") {
        // draw 
        return draw_choice[opp_choice];
    }
    else {
        // win 
        return win_choice[opp_choice];
    }
}

var total_score = 0;
for (let i=0;i<rounds.length; i++) {
    var choices = rounds[i].split(" ");
    var opp_choice = choices[0];
    var your_strategy = choices[1];

    let command = get_command(your_strategy, opp_choice);
    let score = strategy_score[your_strategy] + choice_value[command];
    total_score += score;
}

print(total_score);
