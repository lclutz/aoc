import math


ifile = "input.txt"


class Direction:
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Boat:

    def __init__(self):
        self.direction = (1, 0)
        self.position = (0, 0)

    def rotate(self, degrees):
        rads = math.radians(degrees)
        x, y = self.direction
        c = math.cos(rads)
        s = math.sin(rads)
        new_x = x * c - y * s
        new_y = x * s + y * c
        self.direction = (new_x, new_y)

    def forward(self, value):
        new_x = self.position[0] + self.direction[0] * value
        new_y = self.position[1] + self.direction[1] * value
        self.position = (new_x, new_y)

    def move(self, direction, value):
        x, y = self.position
        if direction == Direction.NORTH:
            y += value
        elif direction == Direction.EAST:
            x += value
        elif direction == Direction.SOUTH:
            y -= value
        elif direction == Direction.WEST:
            x -= value
        self.position = (x, y)

    def do(self, instruction):
        itype, ivalue = instruction
        if itype == 'F':
            self.forward(ivalue)
        elif itype == 'R':
            self.rotate(-ivalue)
        elif itype == 'L':
            self.rotate(ivalue)
        elif itype == 'N':
            self.move(Direction.NORTH, ivalue)
        elif itype == 'E':
            self.move(Direction.EAST, ivalue)
        elif itype == 'S':
            self.move(Direction.SOUTH, ivalue)
        elif itype == 'W':
            self.move(Direction.WEST, ivalue)


with open(ifile, mode="r") as f:
    puzzle_input = [(line[0], int(line[1:])) for line in f]

b = Boat()
for instruction in puzzle_input:
    b.do(instruction)

manhatten_distance = abs(b.position[0]) + abs(b.position[1])

print(f"part1: {int(manhatten_distance)}")


class Boat2:

    def __init__(self):
        self.waypoint = (10, 1)
        self.position = (0, 0)

    def rotate_waypoint(self, degrees):
        x, y = self.waypoint
        rads = math.radians(degrees)
        c = math.cos(rads)
        s = math.sin(rads)
        new_x = x * c - y * s
        new_y = x * s + y * c
        self.waypoint = (new_x, new_y)

    def forward(self, value):
        dx, dy = self.waypoint
        px = self.position[0] + value * dx
        py = self.position[1] + value * dy
        self.position = (px, py)

    def move_waypoint(self, direction, value):
        x, y = self.waypoint
        if direction == Direction.NORTH:
            y += value
        elif direction == Direction.EAST:
            x += value
        elif direction == Direction.SOUTH:
            y -= value
        elif direction == Direction.WEST:
            x -= value
        self.waypoint = (x, y)

    def do(self, instruction):
        itype, ivalue = instruction
        if itype == 'F':
            self.forward(ivalue)
        elif itype == 'R':
            self.rotate_waypoint(-ivalue)
        elif itype == 'L':
            self.rotate_waypoint(ivalue)
        elif itype == 'N':
            self.move_waypoint(Direction.NORTH, ivalue)
        elif itype == 'E':
            self.move_waypoint(Direction.EAST, ivalue)
        elif itype == 'S':
            self.move_waypoint(Direction.SOUTH, ivalue)
        elif itype == 'W':
            self.move_waypoint(Direction.WEST, ivalue)


b2 = Boat2()
for instruction in puzzle_input:
    b2.do(instruction)

manhatten_distance = abs(b2.position[0]) + abs(b2.position[1])

print(f"part2: {int(manhatten_distance)}")
