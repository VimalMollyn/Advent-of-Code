def find_xmas_count(grid):
    """
    Searches a grid for all occurrences of "X-MAS" patterns (two MAS or SAM forming an X) and returns the count.

    Args:
        grid: A list of strings, where each string is a row in the grid.

    Returns:
        The number of times "X-MAS" appears in the grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    targets = ["MAS", "SAM"]

    for r in range(rows):
        for c in range(cols):
            for dx1, dy1 in [(1, 1), (1, -1)]:
                for dx2, dy2 in [(1, -1), (-1, -1)]:
                    if (dx1, dy1) == (-dx2, -dy2):
                        continue

                    x_shape = ""
                    valid_x = True
                    # Build X shape
                    for i in range(3):
                        nr1 = r + i * dx1
                        nc1 = c + i * dy1
                        nr2 = r + i * dx2
                        nc2 = c + i * dy2

                        if nr1 < 0 or nr1 >= rows or nc1 < 0 or nc1 >= cols:
                            valid_x = False
                            break
                        if nr2 < 0 or nr2 >= rows or nc2 < 0 or nc2 >= cols:
                             valid_x = False
                             break
                        if i != 1:
                            x_shape += grid[nr1][nc1]
                            x_shape += grid[nr2][nc2]
                        else:
                           if grid[nr1][nc1] != grid[nr2][nc2]:
                             valid_x = False
                             break

                    if valid_x:
                        #Explicitly check all orientations
                        for t1 in targets:
                          for t2 in targets:
                            if x_shape[0:3] == t1 and x_shape[3:6] == t2:
                                count+=1
                            elif x_shape[0:3] == t2[::-1] and x_shape[3:6] == t1: # flipped 1st
                                count+=1
                            elif x_shape[0:3] == t1 and x_shape[3:6] == t2[::-1]: # flipped 2nd
                                count+=1
                            elif x_shape[0:3] == t2[::-1] and x_shape[3:6] == t1[::-1]:# flipped both
                                count+=1
    return count


if __name__ == "__main__":
    # Read input from file
    with open("input.txt", "r") as f:
        grid = [line.strip() for line in f.readlines()]

    xmas_count = find_xmas_count(grid)
    print(f"The number of times X-MAS appears is: {xmas_count}")