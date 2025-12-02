def find_xmas_count(grid):
    """
    Searches a grid for all occurrences of "XMAS" in all directions and returns the count.

    Args:
        grid: A list of strings, where each string is a row in the grid.

    Returns:
        The number of times "XMAS" appears in the grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    target = "XMAS"

    # Directions: right, left, down, up, diagonal_down_right, diagonal_down_left, diagonal_up_right, diagonal_up_left
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                match = True
                for i in range(len(target)):
                    nr, nc = r + i * dr, c + i * dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != target[i]:
                        match = False
                        break # exit loop if we are out of bounds or if char doesn't match
                if match:
                    count += 1

    return count

if __name__ == "__main__":
    # Read input from file
    with open("input.txt", "r") as f:
        grid = [line.strip() for line in f.readlines()]

    xmas_count = find_xmas_count(grid)
    print(f"The number of times XMAS appears is: {xmas_count}")