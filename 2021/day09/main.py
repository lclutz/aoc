ifile = "example.txt"

with open(ifile, mode="r") as f:
    puzzle_input = [[int(i) for i in l.strip()] for l in f]

height = len(puzzle_input)
width = len(puzzle_input[0])

low_points = list()

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
            low_points.append((row, col))

risk_levels = [puzzle_input[row][col] + 1 for row, col in low_points]

print(f"part1: {sum(risk_levels)}")

def measure(row, col):
    result = 0
    visited = set((row, col))
    points_to_check = [(y, x) for (y, x) in
                       [(row - 1, col),
                        (row + 1, col),
                        (row, col - 1),
                        (row, col + 1)]
                       if x >= 0 and x < width and y >= 0 and y < height and (y, x) not in visited]
    while len(points_to_check) != 0:
        new_points_to_check = list()
        for y, x in points_to_check:
            if puzzle_input[y][x] != 9:
                result += 1
                new_points_to_check += [(y2, x2) for (y2, x2) in[
                    (y - 1, x),
                    (y + 1, x),
                    (y, x - 1),
                    (y, x + 1)
                ] if x2 >= 0 and x2 < width and y2 >= 0 and y2 < height]
            visited.add((y, x))
        points_to_check = list(set(new_points_to_check) - visited)
    return result


basin_sizes = [measure(row, col) for row, col in low_points]
basin_sizes.sort(reverse=True)
print(f"part2: {basin_sizes[0] * basin_sizes[1] * basin_sizes[2]}")
