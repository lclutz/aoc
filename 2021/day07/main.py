ifile = "example.txt"

with open(ifile, mode="r") as f:
    puzzle_input = [int(l) for l in f.readline().strip().split(",")]

costs = [sum([abs(xpos - i) for i in puzzle_input])
             for xpos in range(max(puzzle_input))]

print(f"part1: {min(costs)}")

costs = [sum([sum(range(abs(xpos - i) + 1)) for i in puzzle_input])
              for xpos in range(max(puzzle_input))]

print(f"part2: {min(costs)}")
