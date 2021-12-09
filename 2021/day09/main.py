ifile = "example.txt"

with open(ifile, mode="r") as f:
    puzzle_input = [[int(i) for i in l.strip()] for l in f]

height = len(puzzle_input)
width = len(puzzle_input[0])

risk_levels = list()

for row in range(height):
    for col in range(width):
        points_to_check = [(y, x) for (y, x) in
                           [(row - 1, col),
                            (row + 1, col),
                            (row, col - 1),
                            (row, col + 1)]
                           if x >= 0 and x < width and y >= 0 and y < height]

        if all([(puzzle_input[row][col] < puzzle_input[y][x])
                for y, x in points_to_check]):
            risk_levels.append(puzzle_input[row][col] + 1)

print(f"part1: {sum(risk_levels)}")
