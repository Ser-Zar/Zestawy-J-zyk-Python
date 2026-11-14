import pytest
from points import Point

from triangles import Triangle 

def test_triangle_init_and_error():
    t = Triangle(0, 0, 4, 0, 0, 3)
    assert t.area() == 6.0
    
    # Test współliniowości punktów (ValueError)
    with pytest.raises(ValueError):
        Triangle(0, 0, 1, 1, 2, 2)

def test_from_points():
    p1 = Point(0, 0)
    p2 = Point(4, 0)
    p3 = Point(0, 3)
    t = Triangle.from_points((p1, p2, p3))
    assert t.area() == 6.0

def test_equality():
    t1 = Triangle(0, 0, 4, 0, 0, 3)
    t2 = Triangle(0, 3, 0, 0, 4, 0)  # inna kolejność wierzchołków
    assert t1 == t2

def test_bounding_box_properties():
    # Trójkąt o wierzchołkach (1, 1), (5, 1), (3, 4)
    t = Triangle(1, 1, 5, 1, 3, 4)
    
    assert t.left == 1
    assert t.right == 5
    assert t.bottom == 1
    assert t.top == 4
    assert t.width == 4
    assert t.height == 3
    
    assert t.topleft == Point(1, 4)
    assert t.bottomleft == Point(1, 1)
    assert t.topright == Point(5, 4)
    assert t.bottomright == Point(5, 1)