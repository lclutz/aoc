ifile = "example.txt"

with open(ifile, mode="r") as f:
    puzzle_input = [line.strip() for line in f]


fish_timers = [int(t) for t in puzzle_input[0].split(",")]

SPAWN_TIME = 6
SPAWN_TIME_FOR_NEW_FISH = 8

def step(fish_timers):
    new_fish = 0
    for index, fish_timer in enumerate(fish_timers):
        fish_timer -= 1
        if fish_timer < 0:
            fish_timer = SPAWN_TIME
            new_fish += 1
        fish_timers[index] = fish_timer

    for _ in range(new_fish):
        fish_timers.append(SPAWN_TIME_FOR_NEW_FISH)

for _ in range(80):
    step(fish_timers)

print(f"part1: {len(fish_timers)}")
