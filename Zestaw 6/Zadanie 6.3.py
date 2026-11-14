import unittest
from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f"[{self.pt1}, {self.pt2}]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    def center(self):
        # Zwraca środek prostokąta (obiekt klasy Point)
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):
        # Pole powierzchni (liczba)
        return abs((self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y))

    def move(self, x, y):
        # Przesunięcie o wektor (x, y)
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        return self


# Kod testujący moduł.
class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(0, 0, 4, 3)
        self.r2 = Rectangle(0, 0, 4, 3)
        self.r3 = Rectangle(1, 1, 5, 4)

    def test_init_and_str(self):
        self.assertEqual(str(self.r1), "[(0, 0), (4, 3)]")
        self.assertEqual(repr(self.r1), "Rectangle(0, 0, 4, 3)")

    def test_equality(self):
        self.assertEqual(self.r1, self.r2)
        self.assertNotEqual(self.r1, self.r3)

    def test_center(self):
        self.assertEqual(self.r1.center(), Point(2, 1.5))

    def test_area(self):
        self.assertEqual(self.r1.area(), 12)

    def test_move(self):
        self.r1.move(1, 2)
        self.assertEqual(self.r1, Rectangle(1, 2, 5, 5))

if __name__ == "__main__":
    unittest.main()