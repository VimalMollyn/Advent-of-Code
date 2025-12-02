import Foundation

// load the contents of sample_input into a string
let path = "input.txt"

let text = try String(contentsOfFile: path, encoding: .utf8)
// split the string into an array of strings, each string representing a line
let lines = text.components(separatedBy: "\n")

// the text is like this:
// 467..114..
// ...*......
// ..35..633.
// ......#...
// 617*......
// .....+.58.
// ..592.....
// ......755.
// ...$.*....
// .664.598..

// convert the text into a 2D array of characters of size count(lines) x count(lines[0])
var grid = [[Character]]()

// create a data structure to store which indices have which whole number
var numbers = Array(repeating: Array(repeating: 0, count: lines[0].count), count: lines.count)

for line in lines {
    grid.append(Array(line))

    // find the numbers in the line, for example, 467, 114 in "467..114.."
    let regex = try! NSRegularExpression(pattern: "[0-9]+", options: [])
    let matches = regex.matches(in: line, options: [], range: NSRange(location: 0, length: line.count))

    // check if any repeats were found in the line
    var lineMatches = [Int]()
    for match in matches {
        let number = Int((line as NSString).substring(with: match.range))!

        let i = grid.count - 1
        for j in match.range.location..<match.range.location+match.range.length {
            numbers[i][j] = number
        }

        if !lineMatches.contains(number) {
            lineMatches.append(number)
        }
        else {
            print("repeated number \(number) in line \(grid.count)")
        }
    }   
}

let symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "+", "=", "-"]
var total = 0

// loop through the grid
for i in 0..<grid.count {
    var validNumbers = [Int]()
    for j in 0..<grid[i].count {
        let c = grid[i][j]

        // if the character is a symbol
        if symbols.contains(String(c)) {
            // get all the indices around the symbol, including diagonals
            let indices = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]

            // loop through the indices
            for (k, l) in indices {
                // if the index is in bounds
                if k >= 0 && k < grid.count && l >= 0 && l < grid[i].count {
                    // check if the character is a digit
                    if grid[k][l].isNumber {
                        // if it is, get the number at that index
                        let number = numbers[k][l]
                        print(number, k, l)

                        // add it to the list of valid numbers
                        if !validNumbers.contains(number) {
                            validNumbers.append(number)
                        }
                    }
                }
            }
        }
    }
    total += validNumbers.reduce(0, +)
}

print(total + toadd)
