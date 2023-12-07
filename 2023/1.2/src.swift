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

    // replace all occurrences of ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"] with ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    let replacements = [
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    ]

    // for each word in the replacements dict, store the replacement and it's position in the line in a list
    var replacements_list: [(String, String, Int)] = []
    for (word, replacement) in replacements {
        // get all the occurrences of the word in the line
        let occurrences = line.ranges(of: word)

        // for each occurrence, add the word, the replacement, and the position to the list
        for occurrence in occurrences {
            replacements_list.append((word, replacement, occurrence.lowerBound.utf16Offset(in: line)))
        }
    }

    var new_line = line

    // sort the list by position
    replacements_list.sort(by: { $0.2 < $1.2 })

    if (replacements_list.count>=2) {
        // only replace the first and last word in the replacements list
        let first_replacement = replacements_list[0]
        let last_replacement = replacements_list[replacements_list.count - 1]

        // replace the first word
        let first_word = first_replacement.0
        let first_position = first_replacement.2
        new_line.replaceSubrange(new_line.index(new_line.startIndex, offsetBy: first_position)..<new_line.index(new_line.startIndex, offsetBy: first_position + 1), with: first_replacement.1)

        // modify the last position to account for the change in length
        let last_position = last_replacement.2 + (first_replacement.1.count - 1)

        // replace the last word
        let last_word = last_replacement.0
        new_line.replaceSubrange(new_line.index(new_line.startIndex, offsetBy: last_position)..<new_line.index(new_line.startIndex, offsetBy: last_position + 1), with: last_replacement.1)
    } 
    else {
        // replace all words in the replacements list
        for replacement in replacements_list {
            // get the word and position from the replacement
            let word = replacement.0
            let position = replacement.2

            // replace the word with the replacement
            new_line.replaceSubrange(new_line.index(new_line.startIndex, offsetBy: position)..<new_line.index(new_line.startIndex, offsetBy: position + 1), with: replacement.1)
        }
    }
    print("line: \(line), new_line: \(new_line), replacements_list: \(replacements_list)")

    for char in new_line {
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