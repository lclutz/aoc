
ifile = "example.txt"

with open(ifile, mode="r") as f:
    puzzle_input = [int(line) for line in f]

measurement_increases = sum([1 if puzzle_input[i] < puzzle_input[i + 1] else 0
                             for i in range(len(puzzle_input) - 1)])

print(f"part1: {measurement_increases}")

sums = [sum(puzzle_input[i:i+3]) for i in range(len(puzzle_input) - 2)]

sum_increases = sum([1 if sums[i] < sums[i + 1] else 0
                     for i in range(len(sums) - 1)])

print(f"part2: {sum_increases}")
