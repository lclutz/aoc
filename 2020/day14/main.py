import re

ifile = "input.txt"

zero_mask = 2 ** 36 - 1
one_mask  = 0

memory = dict()


def set_masks(mask):
    global one_mask, zero_mask
    one_mask = sum([2 ** index for index, val in enumerate(mask[::-1]) if val == "1"])
    zero_mask = sum([2 ** index for index, val in enumerate(mask[::-1]) if val != "0"])


def write_memory(addr, val):
    val |= one_mask
    val &= zero_mask
    memory[addr] = val


with open(ifile, mode="r") as f:
    lines = [line.strip() for line in f]

for line in lines:
    m = re.match(r"^mask = (.*)$", line)
    if m:
        set_masks(m.group(1))

    m = re.match(r"^mem\[(.*)\] = (.*)$", line)
    if m:
        write_memory(int(m.group(1)), int(m.group(2)))

print(f"part1: {sum(memory.values())}")

one_mask = 0
zero_mask = 2 ** 26 - 1
floating_offsets = []

memory = dict()


def set_masks2(mask):
    global one_mask, zero_mask, floating_offsets
    floating_offsets = []
    one_mask = sum([2 ** index for index, val in enumerate(mask[::-1]) if val == "1"])
    zero_mask = sum([2 ** index for index, val in enumerate(mask[::-1]) if val != "X"])
    floating = [2 ** index for index, val in enumerate(mask[::-1]) if val == "X"]
    floating_masks = list(range(2 ** len(floating)))
    for floating_mask in floating_masks:
        floating_offsets.append(sum([ val for index, val in enumerate(floating) if (2 ** index & floating_mask) != 0 ]))


def write_memory2(addr, val):
    addr |= one_mask
    addr &= zero_mask
    addresses = [addr + floating_offset for floating_offset in floating_offsets]
    for address in addresses:
        memory[address] = val


for line in lines:
    m = re.match(r"^mask = (.*)$", line)
    if m:
        set_masks2(m.group(1))

    m = re.match(r"^mem\[(.*)\] = (.*)$", line)
    if m:
        write_memory2(int(m.group(1)), int(m.group(2)))

print(f"part2: {sum(memory.values())}")
