import sys

sys.path.append("../")

import triangle

def test_area():
    i, j, k = 5, 4, 5
    area = triangle.area(i, j, k)
    assert area == 9.16515138991168

def test_perimeter():
    i, j, k = 2, 2, 2
    perimeter = triangle.perimeter(i, j, k)
    assert perimeter == 6


