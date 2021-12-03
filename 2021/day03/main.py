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
    if ones_minus_zeros >= 0:
        most_common_bits.append(1)
    else:
        most_common_bits.append(0)

gamma_rate = reduce(lambda x, y: x + (2 ** y[0]) * y[1],
                    enumerate(most_common_bits), 0)

epsilon_rate = gamma_rate ^ (2 ** bit_len - 1)

power_consumption = gamma_rate * epsilon_rate

print(f"part1: {power_consumption}")

def find_most_common_bit(numbers, position):
    ones_minus_zeros = 0
    for number in numbers:
        if (2 ** position) & number != 0:
            ones_minus_zeros += 1
        else:
            ones_minus_zeros -= 1
    return 1 if ones_minus_zeros >= 0 else 0

oxygen_numbers = numbers

for i in range(bit_len - 1, -1, -1):
    criteria = find_most_common_bit(oxygen_numbers, i)
    if criteria == 1:
        oxygen_numbers = list(filter(lambda x: x & (2 ** i) != 0, oxygen_numbers))
    else:
        oxygen_numbers = list(filter(lambda x: x & (2 ** i) == 0, oxygen_numbers))

    if len(oxygen_numbers) <= 1:
        break

oxygen_number = oxygen_numbers[0]

def find_least_common_bit(numbers, position):
    ones_minus_zeros = 0
    for number in numbers:
        if (2 ** position) & number != 0:
            ones_minus_zeros += 1
        else:
            ones_minus_zeros -= 1
    return 1 if ones_minus_zeros < 0 else 0

co2_numbers = numbers

for i in range(bit_len - 1, -1, -1):
    criteria = find_least_common_bit(co2_numbers, i)
    if criteria == 1:
        co2_numbers = list(filter(lambda x: x & (2 ** i) != 0, co2_numbers))
    else:
        co2_numbers = list(filter(lambda x: x & (2 ** i) == 0, co2_numbers))

    if len(co2_numbers) <= 1:
        break

co2_number = co2_numbers[0]

life_support_rating = oxygen_number * co2_number

print(f"part2: {life_support_rating}")
