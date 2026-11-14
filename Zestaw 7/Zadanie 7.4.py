import math
import unittest
from points import Point

class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)
        
        if self.area() == 0:
            raise ValueError("Punkty są współliniowe - nie tworzą trójkąta.")

    def __str__(self):
        return f"[{self.pt1}, {self.pt2}, {self.pt3}]"

    def __repr__(self):
        return f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})"

    def __eq__(self, other):
        # Trójkąty powinny być równe, jeżeli mają ten sam zbiór wierzchołków,
        # niezależnie od kolejności punktów w atrybutach pt1, pt2, pt3.
        self_set = {self.pt1, self.pt2, self.pt3}
        other_set = {other.pt1, other.pt2, other.pt3}
        return self_set == other_set

    def __ne__(self, other):
        return not self == other

    def center(self):
        # Zwraca środek trójkąta (środki ciężkości / centroid)
        cx = (self.pt1.x + self.pt2.x + self.pt3.x) / 3
        cy = (self.pt1.y + self.pt2.y + self.pt3.y) / 3
        return Point(cx, cy)

    def area(self):
        # Pole powierzchni wzorem wyznacznikowym
        return 0.5 * abs(
            self.pt1.x * (self.pt2.y - self.pt3.y) +
            self.pt2.x * (self.pt3.y - self.pt1.y) +
            self.pt3.x * (self.pt1.y - self.pt2.y)
        )

    def move(self, x, y):
        # Przesunięcie o (x, y)
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        self.pt3.x += x
        self.pt3.y += y
        return self

    def make4(self):
        # Zwraca krotkę czterech mniejszych trójkątów po podziale
        # Środki boków:
        m12 = Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)
        m23 = Point((self.pt2.x + self.pt3.x) / 2, (self.pt2.y + self.pt3.y) / 2)
        m31 = Point((self.pt3.x + self.pt1.x) / 2, (self.pt3.y + self.pt1.y) / 2)
        
        t1 = Triangle(self.pt1.x, self.pt1.y, m12.x, m12.y, m31.x, m31.y)
        t2 = Triangle(m12.x, m12.y, self.pt2.x, self.pt2.y, m23.x, m23.y)
        t3 = Triangle(m31.x, m31.y, m23.x, m23.y, self.pt3.x, self.pt3.y)
        t4 = Triangle(m12.x, m12.y, m23.x, m23.y, m31.x, m31.y)
        
        return (t1, t2, t3, t4)


# Kod testujący moduł.
class TestTriangle(unittest.TestCase):
    def test_init_valid_and_invalid(self):
        t = Triangle(0, 0, 4, 0, 0, 3)
        self.assertEqual(t.area(), 6.0)
        # Punkty współliniowe powinny wyrzucić ValueError
        with self.assertRaises(ValueError):
            Triangle(0, 0, 1, 1, 2, 2)

    def test_equality_different_order(self):
        t1 = Triangle(0, 0, 4, 0, 0, 3)
        t2 = Triangle(0, 3, 0, 0, 4, 0)  # inna kolejność wierzchołków
        self.assertEqual(t1, t2)

    def test_center_and_move(self):
        t = Triangle(0, 0, 3, 0, 0, 3)
        self.assertEqual(t.center(), Point(1, 1))
        t.move(1, 1)
        self.assertEqual(t, Triangle(1, 1, 4, 1, 1, 4))

    def test_make4(self):
        t = Triangle(0, 0, 4, 0, 0, 4)
        smaller = t.make4()
        self.assertEqual(len(smaller), 4)
        for sub_t in smaller:
            self.assertEqual(sub_t.area(), t.area() / 4)

if __name__ == "__main__":
    unittest.main()