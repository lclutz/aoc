ifile = "example.txt"

with open(ifile, mode="r") as f:
    puzzle_input = [int(l) for l in f.readline().strip().split(",")]

costs = list()
for p in range(max(puzzle_input)):
    cost = sum([abs(i - p) for i in puzzle_input])
    costs.append(cost)

print(f"part1: {min(costs)}")

costs = list()
for p in range(max(puzzle_input)):
    cost = sum([sum(range(abs(i - p) + 1)) for i in puzzle_input])
    costs.append(cost)

print(f"part2: {min(costs)}")
