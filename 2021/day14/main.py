ifile = "example.txt"

with open(ifile, mode="r") as f:
    puzzle_input = [line.strip() for line in f]

polymer_template = puzzle_input[0]
last_character = polymer_template[-1]
insertion_rules = dict()

for line in puzzle_input[2:]:
    k, v = line.split(" -> ")
    insertion_rules[k] = v

pairs = {pair: 0 for pair in insertion_rules.keys()}
for i in range(len(polymer_template) - 1):
    pair = polymer_template[i:i + 2]
    if pair in pairs:
        pairs[pair] += 1
    else:
        pairs[pair] = 1


def step():
    global pairs
    new_pairs = dict()
    for pair, count in pairs.items():
        replacements = [pair[0] + insertion_rules[pair],
                        insertion_rules[pair] + pair[1]]
        for replacement in replacements:
            if replacement not in new_pairs:
                new_pairs[replacement] = count
            else:
                new_pairs[replacement] += count
    pairs = new_pairs


for _ in range(10):
    step()

letters = set("".join([pair[0] for pair in pairs.keys()]))
counts = dict()

for letter in letters:
    for pair, count in pairs.items():
        if letter == pair[0]:
            if letter in counts:
                counts[letter] += count
            else:
                counts[letter] = count

counts[last_character] += 1

print(f"part1: {max(counts.values()) - min(counts.values())}")

for _ in range(30):
    step()

letters = set("".join([pair[0] for pair in pairs.keys()]))
counts = dict()

for letter in letters:
    for pair, count in pairs.items():
        if letter == pair[0]:
            if letter in counts:
                counts[letter] += count
            else:
                counts[letter] = count

counts[last_character] += 1

print(f"part2: {max(counts.values()) - min(counts.values())}")
