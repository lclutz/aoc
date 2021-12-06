ifile = "example.txt"

with open(ifile, mode="r") as f:
    puzzle_input = [line.strip() for line in f]

fish_timers = [0 for _ in range(9)]

for timer in [int(t) for t in puzzle_input[0].split(",")]:
    fish_timers[timer] += 1

def step(fish_timers):
    new_fish_timers = [0 for _ in range(9)]
    new_fish_timers[8] = fish_timers[0]
    new_fish_timers[6] = fish_timers[0]
    for i in range(1, 9):
        new_fish_timers[i-1] += fish_timers[i]
    return new_fish_timers

for _ in range(80):
    fish_timers = step(fish_timers)

print(f"part1: {sum(fish_timers)}")

for _ in range(256 - 80):
    fish_timers = step(fish_timers)

print(f"part2: {sum(fish_timers)}")
