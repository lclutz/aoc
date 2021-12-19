from math import floor, ceil

ifile = "example.txt"


class Node:

    def __init__(self, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"[{self.left},{self.right}]"

    def __add__(self, other):
        n = Node(left=self, right=other)
        n.left.parent = n
        n.right.parent = n
        node_to_explode = n.explosion_pending()
        node_to_split = n.explosion_pending()
        while node_to_explode or node_to_split:
            if node_to_explode:
                node_to_explode.explode()
                node_to_explode = n.explosion_pending()
                node_to_split = n.split_pending()
                continue
            if node_to_split:
                node_to_split.split()
                node_to_explode = n.explosion_pending()
                node_to_split = n.split_pending()
        return n

    def split(self):
        if isinstance(self.left, int) and self.left >= 10:
            self.left = Node(left=floor(self.left/2), right=ceil(self.left/2), parent=self)
        elif isinstance(self.right, int) and self.right >= 10:
            self.right = Node(left=floor(self.right/2), right=ceil(self.right/2), parent=self)

    def split_pending(self):
        if isinstance(self.left, int) and self.left >= 10:
            return self
        if isinstance(self.right, int) and self.right >= 10:
            return self
        if isinstance(self.left, Node):
            split_pending_left = self.left.split_pending()
            if split_pending_left:
                return split_pending_left
        if isinstance(self.right, Node):
            split_pending_right = self.right.split_pending()
            if split_pending_right:
                return split_pending_right
        return None

    def explode(self):
        p = self.parent
        direct_predecessor = self
        pleft = pright = None
        while p and not (pleft and pright):
            if (not pleft) and not (p.left is direct_predecessor):
                if isinstance(p.left, Node):
                    pleft = p.left
                else:
                    pleft = p
            if (not pright) and not (p.right is direct_predecessor):
                if isinstance(p.right, Node):
                    pright = p.right
                else:
                    pright = p
            direct_predecessor = p
            p = p.parent
        if pleft:
            pleft = pleft.find_right_most_node_for_explosion()
            if isinstance(pleft.right, int):
                pleft.right += self.left
            else:
                pleft.left += self.left
        if pright:
            pright = pright.find_left_most_node_for_explosion()
            if isinstance(pright.left, int):
                pright.left += self.right
            else:
                pright.right += self.right

        if self.parent.left is self:
            self.parent.left = 0
        else:
            self.parent.right = 0

    def find_right_most_node_for_explosion(self):
        if isinstance(self.right, int):
            return self
        if isinstance(self.left, int):
            return self
        if isinstance(self.right, Node):
            right_search = self.right.find_right_most_node_for_explosion()
            if right_search:
                return right_search
        if isinstance(self.left, Node):
            left_search = self.left.find_right_most_node_for_explosion()
            if left_search:
                return left_search

    def find_left_most_node_for_explosion(self):
        if isinstance(self.left, int):
            return self
        if isinstance(self.right, int):
            return self
        if isinstance(self.left, Node):
            left_search = self.left.find_left_most_node_for_explosion()
            if left_search:
                return left_search
        if isinstance(self.right, Node):
            right_search = self.right.find_left_most_node_for_explosion()
            if right_search:
                return right_search

    def explosion_pending(self, depth=0):
        if not (isinstance(self.left, int) and isinstance(self.right, int)):
            if isinstance(self.left, Node):
                explosion_pending_left = self.left.explosion_pending(depth + 1)
                if explosion_pending_left:
                    return explosion_pending_left
            if isinstance(self.right, Node):
                explosion_pending_right = self.right.explosion_pending(depth + 1)
                if explosion_pending_right:
                    return explosion_pending_right
            return None
        else:
            return self if depth >= 4 else None

    def magnitude(self):
        magnitude_left, magnitude_right = self.left, self.right
        if isinstance(self.left, Node):
            magnitude_left = self.left.magnitude()
        if isinstance(self.right, Node):
            magnitude_right = self.right.magnitude()
        return 3 * magnitude_left + 2 * magnitude_right


def lists_to_tree(ls, parent=None):
    assert(len(ls) == 2)
    n = Node()
    l, r = ls
    if isinstance(l, list):
        l = lists_to_tree(l, n)
    if isinstance(r, list):
        r = lists_to_tree(r, n)
    n.left = l
    n.right = r
    n.parent = parent
    return n


def tests():
    a = lists_to_tree([[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]])
    b = lists_to_tree([7,[[[3,7],[4,3]],[[6,3],[8,8]]]])
    print(f"  {a}")
    print(f"+ {b}")
    print(f"= {a + b}")
    print()

    a = lists_to_tree([[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]])
    b = lists_to_tree([[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]])
    print(f"  {a}")
    print(f"+ {b}")
    print(f"= {a + b}")
    print()

    a = lists_to_tree([[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]])
    b = lists_to_tree([[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]])
    print(f"  {a}")
    print(f"+ {b}")
    print(f"= {a + b}")
    print()

    a = lists_to_tree([[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]])
    b = lists_to_tree([7,[5,[[3,8],[1,4]]]])
    print(f"  {a}")
    print(f"+ {b}")
    print(f"= {a + b}")
    print()

    a = lists_to_tree([[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]])
    b = lists_to_tree([[2,[2,2]],[8,[8,1]]])
    print(f"  {a}")
    print(f"+ {b}")
    print(f"= {a + b}")
    print()

    a = lists_to_tree([[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]])
    b = lists_to_tree([2,9])
    print(f"  {a}")
    print(f"+ {b}")
    print(f"= {a + b}")
    print()

    a = lists_to_tree([[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]])
    b = lists_to_tree([1,[[[9,3],9],[[9,0],[0,7]]]])
    print(f"  {a}")
    print(f"+ {b}")
    print(f"= {a + b}")
    print()

    a = lists_to_tree([[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]])
    b = lists_to_tree([[[5,[7,4]],7],1])
    print(f"  {a}")
    print(f"+ {b}")
    print(f"= {a + b}")
    print()

    a = lists_to_tree([[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]])
    b = lists_to_tree([[[[4,2],2],6],[8,7]])
    print(f"  {a}")
    print(f"+ {b}")
    print(f"= {a + b}")


def part1():
    with open(ifile, mode="r") as f:
        puzzle_input = [lists_to_tree(eval(line)) for line in f]

    result = puzzle_input[0]
    for num in puzzle_input[1:]:
        result += num
    print(f"part1: {result.magnitude()}")


tests()
