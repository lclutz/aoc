import re
import math

ifile = "example.txt"

with open(ifile, mode="r") as f:
    puzzle_input = f.readline().strip()

m = re.match(r"^target area: x=(.*)\.\.(.*), y=(.*)\.\.(.*)$", puzzle_input)
txmin, txmax, tymin, tymax = [int(g) for g in m.group(1, 2, 3, 4)]


def step(p, v):
    px, py = p
    vx, vy = v
    p = (px + vx, py + vy)
    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1
    vy -= 1
    v = (vx, vy)
    return (p, v)


vxmin = round(math.sqrt(txmin * 2 + 1/4) - 1/2)
vxmax = round(math.sqrt(txmax * 2 + 1/4) - 1/2)

vymin = -tymax
vymax = -tymin

result = None

for vy in range(vymax, vymin - 1, -1):
    for vx in range(vxmax, vxmin - 1, -1):
        p = (0, 0)
        v = (vx, vy)
        high_y = ((vy + 1) * vy) // 2
        while p[0] <= txmax and p[1] >= tymax:
            p, v = step(p, v)
            px, py = p
            if txmin <= px and px <= txmax and tymin <= py and py <= tymax:
                if not result or high_y > result:
                    result = high_y
                    break

print(f"part1: {result}")
