
ifile = "example.txt"

with open(ifile, mode="r") as f:
    puzzle_input = [int(i) for i in f.readline().strip().split(",")]

cache = {num: idx for idx, num in enumerate(puzzle_input)}

last_number_spoken = puzzle_input[-1]
next_number = 0
if last_number_spoken in puzzle_input[:-2]:
    for i in range(1, len(history)):
        if history[len(history) - i - 1] == last_number_spoken:
            next_number = i
            break

for i in range(len(puzzle_input), 2020 - 1):
    if next_number in cache.keys():
        res = i - cache[next_number]
        cache[next_number] = i
        next_number = res
    else:
        cache[next_number] = i
        next_number = 0

print(f"part1: {next_number}")

for i in range(2020 - 1, 30000000 - 1):
    if next_number in cache.keys():
        res = i - cache[next_number]
        cache[next_number] = i
        next_number = res
    else:
        cache[next_number] = i
        next_number = 0

print(f"part2: {next_number}")
