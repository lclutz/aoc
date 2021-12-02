
ifile = "input.txt"


with open(ifile, mode="r") as f:
    puzzle_input = [[seat for seat in line.strip()] for line in f]


def count_adjecent_occupied(state, y, x):
    adjecent_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                        (0, 1), (1, -1), (1, 0), (1, 1)]

    width = len(state[0])
    height = len(state)

    result = 0
    for x_offset, y_offset in adjecent_offsets:
        new_x = x + x_offset
        new_y = y + y_offset
        if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
            continue
        if state[new_y][new_x] == '#':
            result += 1
    return result


def step(old_state):
    new_state = []
    for y, row in enumerate(old_state):
        new_state.append([])
        for x, seat in enumerate(row):
            if seat == '.':
                new_state[y].append('.')
            if seat == 'L':
                if count_adjecent_occupied(old_state, y, x) == 0:
                    new_state[y].append('#')
                else:
                    new_state[y].append('L')
            if seat == '#':
                if count_adjecent_occupied(old_state, y, x) >= 4:
                    new_state[y].append('L')
                else:
                    new_state[y].append('#')
    return new_state


def count_occupied_seats(state):
    result = 0
    for row in state:
        for seat in row:
            if seat == '#':
                result += 1
    return result


def print_state(state):
    for row in state:
        print("".join(row))


current_state = puzzle_input[:]
next_state = step(puzzle_input[:])


while current_state != next_state:
    current_state = next_state[:]
    next_state = step(current_state)


print(f"part1: {count_occupied_seats(current_state)}")


def count_adjecent_occupied2(state, y, x):
    adjecent_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                        (0, 1), (1, -1), (1, 0), (1, 1)]

    width = len(state[0])
    height = len(state)

    result = 0
    for x_offset, y_offset in adjecent_offsets:
        new_x = x + x_offset
        new_y = y + y_offset

        while new_x >= 0 and new_x < width and new_y >= 0 and new_y < height and state[new_y][new_x] == '.':
            new_x += x_offset
            new_y += y_offset

        if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
            continue

        if state[new_y][new_x] == '#':
            result += 1

    return result


def step2(old_state):
    new_state = []
    for y, row in enumerate(old_state):
        new_state.append([])
        for x, seat in enumerate(row):
            if seat == '.':
                new_state[y].append('.')
            if seat == 'L':
                if count_adjecent_occupied2(old_state, y, x) == 0:
                    new_state[y].append('#')
                else:
                    new_state[y].append('L')
            if seat == '#':
                if count_adjecent_occupied2(old_state, y, x) >= 5:
                    new_state[y].append('L')
                else:
                    new_state[y].append('#')
    return new_state


current_state = puzzle_input[:]
next_state = step2(puzzle_input[:])

while current_state != next_state:
    current_state = next_state[:]
    next_state = step2(current_state)


print(f"part2: {count_occupied_seats(current_state)}")
