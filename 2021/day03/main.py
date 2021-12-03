from functools import reduce

ifile = "example.txt"

with open(ifile, mode="r") as f:
    lines = [line.strip() for line in f]
    numbers = [int(line, base=2) for line in lines]
    bit_len = len(lines[0])

most_common_bits = list()

for i in range(bit_len):
    mask = 2 ** i
    ones_minus_zeros = 0
    for number in numbers:
        if number & mask != 0:
            ones_minus_zeros += 1
        else:
            ones_minus_zeros -= 1
    if ones_minus_zeros > 0:
        most_common_bits.append(1)
    else:
        most_common_bits.append(0)

gamma_rate = reduce(lambda x, y: x + (2 ** y[0]) * y[1],
                    enumerate(most_common_bits), 0)

epsilon_rate = gamma_rate ^ (2 ** bit_len - 1)

power_consumption = gamma_rate * epsilon_rate

print(f"part1: {power_consumption}")
