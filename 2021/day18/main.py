ifile = "example.txt"

with open(ifile, mode="r") as f:
    puzzle_input = [line.strip() for line in f]

class SnailfischNumber:

    def __init__(self, string=""):
        self.numbers = list()
        self.depths = list()

        depth = -1
        for i in range(len(string)):
            if string[i] in "0123456789":
                self.numbers.append(int(string[i]))
                self.depths.append(depth)
            elif string[i] == '[':
                depth += 1
            elif string[i] == ']':
                depth -= 1

    def __repr__(self):
        return str(self.numbers) + str(self.depths)

    def __eq__(self, other):
        if isinstance(other, SnailfischNumber):
            l = min(len(self.numbers), len(other.numbers))
            ns = [self.numbers[i] == other.numbers[i] for i in range(l)]
            ds = [self.depths[i] == other.depths[i] for i in range(l)]
            return all(ns) and all(ds)
        return False

    def __add__(self, other):
        result = SnailfischNumber()
        result.depths.extend([d + 1 for d in self.depths])
        result.depths.extend([d + 1 for d in other.depths])
        result.numbers.extend(self.numbers)
        result.numbers.extend(other.numbers)
        result.reduce()
        return result

    def explode(self):
        for i in range(len(self.depths) - 1):
            if self.depths[i] == self.depths[i + 1] and self.depths[i] >= 4:
                l, r = self.numbers[i], self.numbers[i + 1]
                if i >= 1:
                    self.numbers[i - 1] += l
                if i < (len(self.numbers) - 2):
                    self.numbers[i + 2] += r
                self.numbers[i] = 0
                self.depths[i] -= 1
                del self.numbers[i + 1]
                del self.depths[i + 1]
                return True
        return False

    def split(self):
        for i in range(len(self.numbers)):
            if self.numbers[i] >= 10:
                old_number = self.numbers[i]
                self.numbers[i] = old_number // 2
                self.numbers.insert(i + 1, old_number // 2 + (old_number % 2))
                self.depths[i] += 1
                self.depths.insert(i + 1, self.depths[i])
                return True
        return False

    def reduce(self):
        exploded = splitted = True
        while exploded or splitted:
            exploded = self.explode()
            while exploded:
                exploded = self.explode()
            splitted = self.split()

    def magnitude(self):
        mag = self.numbers.copy()
        depths = self.depths.copy()
        while len(mag) > 1:
            d = max(depths)
            i = 1
            while i < len(mag):
                if depths[i] == d and depths[i] == depths[i - 1]:
                    mag[i - 1] = mag[i - 1] * 3 + mag[i] * 2
                    depths[i - 1] -= 1
                    del mag[i]
                    del depths[i]
                i += 1
        return mag[0]


def part1():
    result = SnailfischNumber(puzzle_input[0])
    for n in puzzle_input[1:]:
        result += SnailfischNumber(n)
    print(f"part1: {result.magnitude()}")


if __name__ == '__main__':
    part1()
