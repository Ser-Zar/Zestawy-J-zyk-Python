import math
import unittest

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstruktor
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        # Iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):
        # Długość wektora
        return math.hypot(self.x, self.y)

    def __hash__(self):
        return hash((self.x, self.y)) 


# Kod testujący moduł.
class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(1, 2)
        self.p2 = Point(4, 6)
        self.p3 = Point(1, 2)

    def test_init_and_str(self):
        self.assertEqual(str(self.p1), "(1, 2)")
        self.assertEqual(repr(self.p1), "Point(1, 2)")

    def test_equality(self):
        self.assertEqual(self.p1, self.p3)
        self.assertNotEqual(self.p1, self.p2)

    def test_operations(self):
        self.assertEqual(self.p1 + self.p2, Point(5, 8))
        self.assertEqual(self.p2 - self.p1, Point(3, 4))
        self.assertEqual(self.p1 * self.p2, 1 * 4 + 2 * 6)  # 16
        self.assertEqual(self.p1.cross(self.p2), 1 * 6 - 2 * 4)  # -2
        self.assertAlmostEqual(Point(3, 4).length(), 5.0)

    def test_hash(self):
        # Test czy punkty mogą być kluczami w słowniku / elementami zbioru
        s = {self.p1, self.p3}
        self.assertEqual(len(s), 1)

if __name__ == "__main__":
    unittest.main()