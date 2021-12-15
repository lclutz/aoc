from dataclasses import dataclass

ifile = "example.txt"

with open(ifile, mode="r") as f:
    puzzle_input = [[int(c) for c in line.strip()] for line in f]

height = len(puzzle_input)
width = len(puzzle_input[0]) if height > 0 else 0
end = (height - 1, width - 1)


def neighbours(y, x, width, height):
    return [(y, x) for y, x in [(y - 1, x),
                                (y + 1, x),
                                (y, x - 1),
                                (y, x + 1)]
            if y >= 0 and y < height and x >= 0 and x < width]


@dataclass
class TableEntrie:
    cost: int = None
    predecessor: tuple = None


done = set()
lookup_table = {(0, 0) : TableEntrie(cost = 0)}
visited = set((0,0))
queue = [(0,0)]

while queue:
    min_idx = 0
    min_cost = lookup_table[queue[0]].cost
    for i in range(len(queue)):
        if lookup_table[queue[i]].cost < min_cost:
            min_cost = lookup_table[queue[i]].cost
            min_idx = i

    selected = queue.pop(min_idx)

    successors = [n for n in neighbours(selected[0], selected[1], width, height)
                  if n not in done]

    for successor in successors:
        y, x = successor
        cost = lookup_table[selected].cost + puzzle_input[y][x]
        if successor not in lookup_table or lookup_table[successor].cost > cost:
            lookup_table[successor] = TableEntrie(cost = cost, predecessor = selected)

    done.add(selected)
    queue += successors
    queue = list(set(queue) - set(done))

print(f"part1: {lookup_table[end].cost}")

for i in range(4):
    for row in puzzle_input[i * height:i * height + height]:
        puzzle_input.append(list(map(lambda x: 1 if x == 9 else x + 1, row)))

for row in puzzle_input:
    for i in range(4):
        row += list(map(lambda x: 1 if x == 9 else x + 1, row[i * width:i * width + width]))

height = len(puzzle_input)
width = len(puzzle_input[0]) if len(puzzle_input) > 0 else 0
end = (height - 1, width - 1)
done = set()
lookup_table = {(0, 0) : TableEntrie(cost = 0)}
visited = set((0,0))
queue = [(0,0)]

while queue:
    min_idx = 0
    min_cost = lookup_table[queue[0]].cost
    for i in range(len(queue)):
        if lookup_table[queue[i]].cost < min_cost:
            min_cost = lookup_table[queue[i]].cost
            min_idx = i

    selected = queue.pop(min_idx)

    successors = [n for n in neighbours(selected[0], selected[1], width, height)
                  if n not in done]

    for successor in successors:
        y, x = successor
        cost = lookup_table[selected].cost + puzzle_input[y][x]
        if successor not in lookup_table or lookup_table[successor].cost > cost:
            lookup_table[successor] = TableEntrie(cost = cost, predecessor = selected)

    done.add(selected)
    queue += successors
    queue = list(set(queue) - set(done))

print(f"part2: {lookup_table[end].cost}")
