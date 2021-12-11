import os

infile = "example.txt"


with open(infile, mode="r") as f:
    puzzle_input = [[int(c) for c in line.strip()] for line in f]


def save_as_ppm(file_path, pixels):
    height = len(pixels)
    width = 0 if height == 0 else len(pixels[0])
    with open(file_path, mode="wb") as f:
        f.write(bytes(f"P6\n{width} {height} 255\n", encoding="ascii"))
        for y in range(height):
            for x in range(width):
                pixel = pixels[y][x]
                color = [(pixel >> (8 * 2)) & 0xFF,
                         (pixel >> (8 * 1)) & 0xFF,
                         (pixel >> (8 * 0)) & 0xFF]
                f.write(bytes(color))


def energy_level_to_greyscale(energy_level):
    b = int(round((0xFF / 9) * energy_level))
    return (b << 8 * 2) | (b << 8 * 1) | b


def neighbours(position, width, height):
    y, x = position
    return [(y, x) for y, x in [(y, x + 1),
                                (y, x - 1),
                                (y + 1, x),
                                (y + 1, x + 1),
                                (y + 1, x - 1),
                                (y - 1, x),
                                (y - 1, x + 1),
                                (y - 1, x - 1)]
            if y >= 0 and y < height and x >= 0 and x < width]


def step(old_energy_levels):
    height = len(old_energy_levels)
    width = 0 if height == 0 else len(old_energy_levels[0])
    next_levels = [[el + 1 for el in row] for row in old_energy_levels]
    flash_map = [[False for _ in row] for row in next_levels]

    while any([num > 9 for row in next_levels for num in row]):
        new_next_levels = next_levels[:]

        for y in range(height):
            for x in range(width):
                num = next_levels[y][x]
                if num > 9:
                    neighbour_positions = neighbours((y, x), width, height)
                    for ny, nx in neighbour_positions:
                        new_next_levels[ny][nx] += 1
                    flash_map[y][x] = True

        for y in range(height):
            for x in range(width):
                if flash_map[y][x]:
                    new_next_levels[y][x] = 0

        next_levels = new_next_levels

    return next_levels


l = puzzle_input[:]
flashes = 0

if not os.path.exists("out"):
    os.mkdir("out")
else:
    for file in os.listdir("out"):
        if file.endswith(".ppm"):
            os.remove(f"out/{file}")

for i in range(100):
    l = step(l)
    flashes += sum([1 for row in l for num in row if num == 0])
    pixels = [[energy_level_to_greyscale(el) for el in row] for row in l]
    save_as_ppm("out/{:04n}.ppm".format(i), pixels)

print(f"part1: {flashes}")

l = puzzle_input[:]
step_num = 0

while not all([num == 0 for row in l for num in row]):
    l = step(l)
    pixels = [[energy_level_to_greyscale(el) for el in row] for row in l]
    save_as_ppm("out/{:04n}.ppm".format(step_num), pixels)
    step_num += 1

print(f"part2: {step_num}")

