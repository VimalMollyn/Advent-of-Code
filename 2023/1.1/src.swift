import Foundation

// load the contents of sample_input into a string
let path = "input.txt"

let text = try String(contentsOfFile: path, encoding: .utf8)
// split the string into an array of strings, each string representing a line
let lines = text.components(separatedBy: "\n")

// for each line, find all the digits
var total = 0
for line in lines {
    // create an empty array to store the digits
    var digits_list: [String] = []
    for char in line {
        // check if the character is in a list of digits
        if "0123456789".contains(char) {
            // if it is, add it to the list of digits
            digits_list.append(String(char))
        }
    }

    // combine the first and last digits into a number
    let first = digits_list[0]
    let last = digits_list[digits_list.count - 1]

    // create the number by combining the first and last digits
    let number = Int(first + last)!
    print(number)

    // add the number to the total
    total += number
}

// print the total
print("Total: \(total)")