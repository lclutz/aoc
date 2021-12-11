ifile = "example.txt"

with open(ifile, mode="r") as f:
    puzzle_input = [line.strip() for line in f]

openings = "([{<"
closings = ")]}>"

open_close = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

scoring_table = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

syntax_error_score = 0

corruped_lines = list()

for line_number, line in enumerate(puzzle_input):
    stack = list()
    for paran in line:
        if paran in openings:
            stack.append(paran)
        elif paran in closings:
            expectation = open_close[stack.pop()]
            if expectation != paran:
                syntax_error_score += scoring_table[paran]
                corruped_lines.append(line_number)
                break

print(f"part1: {syntax_error_score}")

scoring_table = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

autocomplete_scores = list()

for line_number in range(len(puzzle_input)):
    if line_number in corruped_lines:
        continue

    line = puzzle_input[line_number]
    total_score = 0

    stack = list()
    for paran in line:
        if paran in openings:
            stack.append(paran)
        elif paran in closings:
            stack.pop()

    stack.reverse()
    for c in stack:
        total_score *= 5
        total_score += scoring_table[open_close[c]]
    autocomplete_scores.append(total_score)

autocomplete_scores.sort()
middle_score = autocomplete_scores[len(autocomplete_scores) // 2]

print(f"part2: {middle_score}")
