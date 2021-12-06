ifile = "example.txt"

with open(ifile, mode="r") as f:
    puzzle_input = [line.strip() for line in f]


SPAWN_TIME = 6
SPAWN_TIME_FOR_NEW_FISH = 8
fish_timers = dict()


for timer in [int(t) for t in puzzle_input[0].split(",")]:
    if timer in fish_timers:
        fish_timers[timer] += 1
    else:
        fish_timers[timer] = 1


def step(fish_timers):
    new_fish_timers = dict()
    for timer, count in fish_timers.items():
        if (timer - 1) < 0:
            if SPAWN_TIME in new_fish_timers:
                new_fish_timers[SPAWN_TIME] += count
            else:
                new_fish_timers[SPAWN_TIME] = count
            if SPAWN_TIME_FOR_NEW_FISH in new_fish_timers:
                new_fish_timers[SPAWN_TIME_FOR_NEW_FISH] += count
            else:
                new_fish_timers[SPAWN_TIME_FOR_NEW_FISH] = count
        else:
            if (timer - 1) in new_fish_timers:
                new_fish_timers[timer - 1] += count
            else:
                new_fish_timers[timer - 1] = count
    return new_fish_timers



for _ in range(80):
    fish_timers = step(fish_timers)

print(f"part1: {sum(fish_timers.values())}")

for _ in range(256 - 80):
    fish_timers = step(fish_timers)

print(f"part2: {sum(fish_timers.values())}")

