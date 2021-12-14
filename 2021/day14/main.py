ifile = "example.txt"

with open(ifile, mode="r") as f:
    puzzle_input = [line.strip() for line in f]

polymer_template = puzzle_input[0]
insertion_rules = dict()

for line in puzzle_input[2:]:
    k, v = line.split(" -> ")
    insertion_rules[k] = v


def step(old_string):
    result = old_string[0]
    for i in range(len(old_string) - 1):
        rule = old_string[i:i + 2]
        result += insertion_rules[rule]
        result += old_string[i + 1]
    return result


for _ in range(10):
    polymer_template = step(polymer_template)

counts = [polymer_template.count(c) for c in set(polymer_template)]
print(f"part1: {max(counts) - min(counts)}")
