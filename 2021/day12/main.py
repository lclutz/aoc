ifile = "example.txt"

with open(ifile, mode="r") as f:
    puzzle_input = [line.strip().split("-") for line in f]

connections = dict()

for a, b in puzzle_input:
    if a not in connections:
        connections[a] = {b}
    else:
        connections[a].add(b)

    if b not in connections:
        connections[b] = {a}
    else:
        connections[b].add(a)

for key in connections.keys():
    connections[key] -= {'start'}

connections['end'] = set()


def get_possible_next(path):
    current_node = path[-1]
    result = set()
    for r in connections[current_node]:
        if r.islower() and r in path:
            continue
        else:
            result.add(r)
    return result


paths = [["start"]]
num_paths_found = 0

while len(paths) != 0:
    new_paths = list()
    for path in paths:
        possible_nexts = get_possible_next(path)
        for possible_next in possible_nexts:
            if possible_next == "end":
                num_paths_found += 1
            else:
                new_paths.append(path + [possible_next])
    paths = new_paths

print(f"part1: {num_paths_found}")


def get_possible_next2(path):
    current_node = path[-1]
    result = set()
    small_caves_visited = [c for c in path if c.islower()]
    small_cave_visited_twice = any([small_caves_visited.count(c) > 1
                                    for c in small_caves_visited ])
    for r in connections[current_node]:
        if r.islower() and (r not in path or not small_cave_visited_twice):
            result.add(r)
        if r.isupper():
            result.add(r)
    return result


paths = [["start"]]
num_paths_found = 0

while len(paths) != 0:
    new_paths = list()
    for path in paths:
        possible_nexts = get_possible_next2(path)
        for possible_next in possible_nexts:
            if possible_next == "end":
                num_paths_found += 1
            else:
                new_paths.append(path + [possible_next])
    paths = new_paths

print(f"part2: {num_paths_found}")
