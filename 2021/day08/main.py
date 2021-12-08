ifile = "example.txt"

with open(ifile, mode="r") as f:
    puzzle_input = [line.strip() for line in f]

result = 0
for line in puzzle_input:
    output_digits = line[line.index("|") + 1:].split()
    for output_digit in output_digits:
        if len(output_digit) in [2,4,3,7]:
            result += 1

print(f"part1: {result}")

output_values = list()
for line in puzzle_input:
    mapping = {l: None for l in "abcdefg"}
    split_index = line.index("|")
    patterns = line[:split_index].split()
    output_digits = line[split_index + 1:].split()

    one_pattern = [p for p in patterns if len(p) == 2][0]
    patterns.remove(one_pattern)
    seven_pattern = [p for p in patterns if len(p) == 3][0]
    patterns.remove(seven_pattern)
    four_pattern = [p for p in patterns if len(p) == 4][0]
    patterns.remove(four_pattern)
    eight_pattern = [p for p in patterns if len(p) == 7][0]
    patterns.remove(eight_pattern)
    nine_pattern = [p for p in patterns if len(p) == 6 and all([l in p for l in four_pattern])][0]
    patterns.remove(nine_pattern)
    mapping['e'] = (set(eight_pattern) - set(nine_pattern)).pop()
    mapping['g'] = ((set(nine_pattern) - set(seven_pattern) - set(four_pattern))).pop()
    mapping['a'] = ((set(nine_pattern) - set(four_pattern)) - set(mapping['g'])).pop()
    two_pattern = [p for p in patterns if len(p) == 5 and all(m in p for m in [mapping['e'], mapping['g'], mapping['a']])][0]
    patterns.remove(two_pattern)
    mapping['b'] = ((set(nine_pattern) - set(two_pattern)) - set(one_pattern)).pop()
    three_pattern = [p for p in patterns if len(p) == 5 and mapping['b'] not in p][0]
    patterns.remove(three_pattern)
    five_pattern = [p for p in patterns if len(p) == 5][0]
    patterns.remove(five_pattern)
    mapping['c'] = (set(nine_pattern) - set(five_pattern)).pop()
    six_pattern = [p for p in patterns if mapping['c'] not in p][0]
    patterns.remove(six_pattern)
    zero_pattern = patterns[0]
    mapping['d'] = (set(eight_pattern) - set(zero_pattern)).pop()
    mapping['f'] = (set(three_pattern) - set(two_pattern)).pop()

    unscrambled_outputs = list()
    for output_digit in output_digits:
        if set(output_digit) == set(zero_pattern):
            unscrambled_outputs.append(0)
        elif set(output_digit) == set(one_pattern):
            unscrambled_outputs.append(1)
        elif set(output_digit) == set(two_pattern):
            unscrambled_outputs.append(2)
        elif set(output_digit) == set(three_pattern):
            unscrambled_outputs.append(3)
        elif set(output_digit) == set(four_pattern):
            unscrambled_outputs.append(4)
        elif set(output_digit) == set(five_pattern):
            unscrambled_outputs.append(5)
        elif set(output_digit) == set(six_pattern):
            unscrambled_outputs.append(6)
        elif set(output_digit) == set(seven_pattern):
            unscrambled_outputs.append(7)
        elif set(output_digit) == set(eight_pattern):
            unscrambled_outputs.append(8)
        elif set(output_digit) == set(nine_pattern):
            unscrambled_outputs.append(9)
        else:
            print(f"unknown pattern: {output_digit}")
    unscrambled_outputs.reverse()
    output_values.append(sum([v * (10 ** i) for i, v in enumerate(unscrambled_outputs)]))

print(f"part2: {sum(output_values)}")
