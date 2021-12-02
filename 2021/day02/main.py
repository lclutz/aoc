
ifile = "example.txt"

with open(ifile, mode="r") as f:
    puzzle_input = [line.strip().split() for line in f]

x = 0
y = 0

for command, value in puzzle_input:
    value = int(value)
    if command == "forward":
        x += value
    elif command == "down":
        y -= value
    elif command == "up":
        y += value

print(f"part1: {abs(x) * abs(y)}")


x = 0
aim = 0
depth = 0

for command, value in puzzle_input:
    value = int(value)
    if command == "forward":
        x += value
        depth += aim * value
    if command == "down":
        aim += value
    if command == "up":
        aim -= value

print(f"part2: {x * depth}")
