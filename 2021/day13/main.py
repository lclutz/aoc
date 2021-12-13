ifile = "input.txt"

with open(ifile, mode="r") as f:
    puzzle_input = [line.strip() for line in f]

dots = [(int(y), int(x)) for x, y in
        [line.split(',') for line in puzzle_input if ',' in line]]
width = max([x for _, x in dots]) + 1
height = max([y for y, _ in dots]) + 1
instructions = [line for line in puzzle_input if "fold" in line]

field = [["." for _ in range(width)] for _ in range(height)]

for y in range(height):
    for x in range(width):
        if (y, x) in dots:
            field[y][x] = "#"

instruction = instructions[0]
ax, idx = instruction.split("=")
idx = int(idx)
ax = ax[-1]
new_field = list()
cells_to_copy = list()
hdiff = 0
wdiff = 0
if ax == "y":
    oben = field[:idx]
    unten = field[idx + 1:]
    unten.reverse()
    if len(oben) >= len(unten):
        new_field = oben
        height = len(oben)
        cells_to_copy = unten
        hdiff = len(oben) - len(unten)
    else:
        new_field = unten
        height = len(unten)
        cells_to_copy = oben
        hdiff = len(unten) - len(oben)
    for y in range(len(cells_to_copy)):
        for x in range(width):
            nf = new_field[y + hdiff][x]
            ctc = cells_to_copy[y][x]
            if nf == "#" or ctc == "#":
                new_field[y + hdiff][x] = "#"
    field = new_field
else:
    links = [row[:idx] for row in field]
    rechts = [row[idx + 1:] for row in field]
    for row in rechts:
        row.reverse()
    if len(links[0]) >= len(rechts[0]):
        new_field = links
        width = len(links[0])
        cells_to_copy = rechts
        wdiff = len(links[0]) - len(rechts[0])
    else:
        new_field = rechts
        width = len(rechts[0])
        cells_to_copy = links
        wdiff = len(rechts[0]) - len(links[0])
    for y in range(height):
        for x in range(len(cells_to_copy[0])):
            nf = new_field[y][x + wdiff]
            ctc = cells_to_copy[y][x]
            if nf == "#" or ctc == "#":
                new_field[y][x + wdiff] = "#"
    field = new_field

num_dots = sum([1 for line in field for c in line if c == "#"])
print(f"part1: {num_dots}")


for instruction in instructions[1:]:
    ax, idx = instruction.split("=")
    idx = int(idx)
    ax = ax[-1]
    new_field = list()
    cells_to_copy = list()
    hdiff = 0
    wdiff = 0
    if ax == "y":
        oben = field[:idx]
        unten = field[idx + 1:]
        unten.reverse()
        if len(oben) >= len(unten):
            new_field = oben
            height = len(oben)
            cells_to_copy = unten
            hdiff = len(oben) - len(unten)
        else:
            new_field = unten
            height = len(unten)
            cells_to_copy = oben
            hdiff = len(unten) - len(oben)
        for y in range(len(cells_to_copy)):
            for x in range(width):
                nf = new_field[y + hdiff][x]
                ctc = cells_to_copy[y][x]
                if nf == "#" or ctc == "#":
                    new_field[y + hdiff][x] = "#"
        field = new_field
    else:
        links = [row[:idx] for row in field]
        rechts = [row[idx + 1:] for row in field]
        for row in rechts:
            row.reverse()
        if len(links[0]) >= len(rechts[0]):
            new_field = links
            width = len(links[0])
            cells_to_copy = rechts
            wdiff = len(links[0]) - len(rechts[0])
        else:
            new_field = rechts
            width = len(rechts[0])
            cells_to_copy = links
            wdiff = len(rechts[0]) - len(links[0])
        for y in range(height):
            for x in range(len(cells_to_copy[0])):
                nf = new_field[y][x + wdiff]
                ctc = cells_to_copy[y][x]
                if nf == "#" or ctc == "#":
                    new_field[y][x + wdiff] = "#"
        field = new_field

print()
for row in field:
    print("".join(row))
