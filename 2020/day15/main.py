
ifile = "example.txt"

with open(ifile, mode="r") as f:
    puzzle_input = [int(i) for i in f.readline().strip().split(",")]

def say_next(history):
    last_number_spoken = history[-1]
    was_spoken_for_the_first_time = last_number_spoken not in history[:-1]
    if was_spoken_for_the_first_time:
        return 0
    else:
        for i in range(1, len(history)):
            if history[len(history) - i - 1] == last_number_spoken:
                return i


for i in range(2020 - len(puzzle_input)):
    puzzle_input.append(say_next(puzzle_input))

print(f"part1: {puzzle_input[-1]}")
