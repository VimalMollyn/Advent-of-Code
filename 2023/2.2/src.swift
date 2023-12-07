import Foundation

// load the contents of sample_input into a string
let path = "input.txt"

let text = try String(contentsOfFile: path, encoding: .utf8)
// split the string into an array of strings, each string representing a line
let lines = text.components(separatedBy: "\n")

// each line is like this
// Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
// for each line, get the game number, and the list of rolls [R, G, B]. if R, G, or B is not there, mark as 0
var games: [(Int, [Int])] = []

var valid_games: [Int] = []

for line in lines {
    // split the line into the game number and the rolls
    let split_line = line.components(separatedBy: ": ")
    let game_number = Int(split_line[0].components(separatedBy: " ")[1])!
    let rolls = split_line[1].components(separatedBy: "; ")

    var min_red = 0
    var min_green = 0
    var min_blue = 0

    for roll in rolls {
        // split the roll by ","
        let comma_split_roll = roll.components(separatedBy: ", ")

        for split_roll in comma_split_roll {
            // split the roll by " "
            let space_split_roll = split_roll.components(separatedBy: " ")

            // get the number and color
            let number = Int(space_split_roll[0])!
            let color = space_split_roll[1]

            // check the number of the color is less than the total of that color
            if(color == "red") {
                if number > min_red {
                    min_red = number
                }
            } else if(color == "green") {
                if number > min_green {
                    min_green = number
                }
            } else if(color == "blue") {
                if number > min_blue {
                    min_blue = number
                }
            }
        }
    }

    var power = min_red * min_green * min_blue
    // append power to valid_games
    valid_games.append(power)

}

print("Valid games: \(valid_games)")

// get the sum of the valid game ids
var sum = 0
for game in valid_games {
    sum += game
}

print("Sum: \(sum)")