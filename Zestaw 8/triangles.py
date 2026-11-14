import math
from points import Point

class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)
        
        if self.area() == 0:
            raise ValueError("Punkty są współliniowe - nie tworzą trójkąta.")

    @classmethod
    def from_points(cls, points):
        """Pozwala utworzyć trójkąt z listy lub krotki zawierającej trzy punkty."""
        p1, p2, p3 = points
        return cls(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y)

    def __str__(self):
        return f"[{self.pt1}, {self.pt2}, {self.pt3}]"

    def __repr__(self):
        return f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})"

    def __eq__(self, other):
        self_set = {self.pt1, self.pt2, self.pt3}
        other_set = {other.pt1, other.pt2, other.pt3}
        return self_set == other_set

    def __ne__(self, other):
        return not self == other

    def center(self):
        cx = (self.pt1.x + self.pt2.x + self.pt3.x) / 3
        cy = (self.pt1.y + self.pt2.y + self.pt3.y) / 3
        return Point(cx, cy)

    def area(self):
        return 0.5 * abs(
            self.pt1.x * (self.pt2.y - self.pt3.y) +
            self.pt2.x * (self.pt3.y - self.pt1.y) +
            self.pt3.x * (self.pt1.y - self.pt2.y)
        )

    def move(self, x, y):
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        self.pt3.x += x
        self.pt3.y += y
        return self

    def make4(self):
        m12 = Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)
        m23 = Point((self.pt2.x + self.pt3.x) / 2, (self.pt2.y + self.pt3.y) / 2)
        m31 = Point(self.pt3.x + self.pt1.x) / 2, (self.pt3.y + self.pt1.y) / 2 if hasattr(self.pt3, 'x') else ...
        # Poprawione współrzędne m31 dla pewności:
        m31 = Point((self.pt3.x + self.pt1.x) / 2, (self.pt3.y + self.pt1.y) / 2)
        
        t1 = Triangle(self.pt1.x, self.pt1.y, m12.x, m12.y, m31.x, m31.y)
        t2 = Triangle(m12.x, m12.y, self.pt2.x, self.pt2.y, m23.x, m23.y)
        t3 = Triangle(m31.x, m31.y, m23.x, m23.y, self.pt3.x, self.pt3.y)
        t4 = Triangle(m12.x, m12.y, m23.x, m23.y, m31.x, m31.y)
        
        return (t1, t2, t3, t4)

    # --- Właściwości wirtualne dla prostokąta ograniczającego (bounding box) ---
    
    @property
    def left(self):
        return min(self.pt1.x, self.pt2.x, self.pt3.x)

    @property
    def right(self):
        return max(self.pt1.x, self.pt2.x, self.pt3.x)

    @property
    def bottom(self):
        return min(self.pt1.y, self.pt2.y, self.pt3.y)

    @property
    def top(self):
        return max(self.pt1.y, self.pt2.y, self.pt3.y)

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        return self.top - self.bottom

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)