import unittest

from main import SnailfischNumber


class MagnitudeTests(unittest.TestCase):

    def test_mag_1(self):
        m = SnailfischNumber("[[1,2],[[3,4],5]]").magnitude()
        self.assertEqual(m, 143)

    def test_mag_2(self):
        m = SnailfischNumber("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]").magnitude()
        self.assertEqual(m, 1384)

    def test_mag_3(self):
        m = SnailfischNumber("[[[[1,1],[2,2]],[3,3]],[4,4]]").magnitude()
        self.assertEqual(m, 445)

    def test_mag_4(self):
        m = SnailfischNumber("[[[[3,0],[5,3]],[4,4]],[5,5]]").magnitude()
        self.assertEqual(m, 791)

    def test_mag_5(self):
        m = SnailfischNumber("[[[[5,0],[7,4]],[5,5]],[6,6]]").magnitude()
        self.assertEqual(m, 1137)

    def test_mag_6(self):
        m = SnailfischNumber("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]").magnitude()
        self.assertEqual(m, 3488)


class ExplosionTests(unittest.TestCase):

    def test_explosion_1(self):
        a = SnailfischNumber("[[[[[9,8],1],2],3],4]")
        b = SnailfischNumber("[[[[0,9],2],3],4]")
        self.assertTrue(a.explode())
        self.assertEqual(a, b)

    def test_explosion_2(self):
        a = SnailfischNumber("[7,[6,[5,[4,[3,2]]]]]")
        b = SnailfischNumber("[7,[6,[5,[7,0]]]]")
        a.explode()
        self.assertEqual(a, b)

    def test_explosion_3(self):
        a = SnailfischNumber("[[6,[5,[4,[3,2]]]],1]")
        b = SnailfischNumber("[[6,[5,[7,0]]],3]")
        self.assertTrue(a.explode())
        self.assertEqual(a, b)

    def test_explosion_4(self):
        a = SnailfischNumber("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
        b = SnailfischNumber("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
        self.assertTrue(a.explode())
        self.assertEqual(a, b)

    def test_explosion_5(self):
        a = SnailfischNumber("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
        b = SnailfischNumber("[[3,[2,[8,0]]],[9,[5,[7,0]]]]")
        self.assertTrue(a.explode())
        self.assertEqual(a, b)


class AdditionTests(unittest.TestCase):

    def test_addition_1(self):
        a = SnailfischNumber("[[[[4,3],4],4],[7,[[8,4],9]]]")
        b = SnailfischNumber("[1,1]")
        c = SnailfischNumber("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")
        self.assertEqual(c, a + b)

    def test_addition_2(self):
        a = SnailfischNumber("[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]")
        b = SnailfischNumber("[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]")
        c = SnailfischNumber("[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]")
        self.assertEqual(c, a + b)

    def test_addition_3(self):
        a = SnailfischNumber("[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]")
        b = SnailfischNumber("[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]")
        c = SnailfischNumber("[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]")
        self.assertEqual(c, a + b)

    def test_addition_4(self):
        a = SnailfischNumber("[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]")
        b = SnailfischNumber("[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]")
        c = SnailfischNumber("[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]")
        self.assertEqual(c, a + b)

    def test_addition_5(self):
        a = SnailfischNumber("[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]")
        b = SnailfischNumber("[7,[5,[[3,8],[1,4]]]]")
        c = SnailfischNumber("[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]")
        self.assertEqual(c, a + b)

    def test_addition_6(self):
        a = SnailfischNumber("[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]")
        b = SnailfischNumber("[[2,[2,2]],[8,[8,1]]]")
        c = SnailfischNumber("[[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]")
        self.assertEqual(c, a + b)

    def test_addition_7(self):
        a = SnailfischNumber("[[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]")
        b = SnailfischNumber("[2,9]")
        c = SnailfischNumber("[[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]")
        self.assertEqual(c, a + b)

    def test_addition_8(self):
        a = SnailfischNumber("[[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]")
        b = SnailfischNumber("[1,[[[9,3],9],[[9,0],[0,7]]]]")
        c = SnailfischNumber("[[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]")
        self.assertEqual(c, a + b)

    def test_addition_9(self):
        a = SnailfischNumber("[[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]")
        b = SnailfischNumber("[[[5,[7,4]],7],1]")
        c = SnailfischNumber("[[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]")
        self.assertEqual(c, a + b)

    def test_addition_10(self):
        a = SnailfischNumber("[[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]")
        b = SnailfischNumber("[[[[4,2],2],6],[8,7]]")
        c = SnailfischNumber("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")
        self.assertEqual(c, a + b)


if __name__ == '__main__':
    unittest.main()
