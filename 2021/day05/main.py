import re
import itertools


ifile = "example.txt"


with open(ifile, mode="r") as f:
    puzzle_input = [line.strip() for line in f]


lines = [[int(x1), int(y1), int(x2), int(y2)]
         for x1, y1, x2, y2 in
         [re.match(r"^([0-9]*),([0-9]*) -> ([0-9]*),([0-9]*)$", line).groups()
             for line in puzzle_input]]


points = list()
for x1, y1, x2, y2 in lines:
    if x1 != x2 and y1 != y2:
        continue

    xrage_begin = x1 if x1 < x2 else x2
    xrage_end = x1 if x1 > x2 else x2

    yrange_begin = y1 if y1 < y2 else y2
    yrange_end = y1 if y1 > y2 else y2

    for x in range(xrage_begin, xrage_end + 1):
        for y in range(yrange_begin, yrange_end + 1):
            points.append((x, y))


counter = dict()
for point in points:
    if point in counter:
        counter[point] += 1
    else:
        counter[point] = 1


min_2_overlap = sum([1 if c >= 2 else 0 for c in counter.values()])
print(f"part1: {min_2_overlap}")
