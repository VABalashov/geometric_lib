import sys

sys.path.append("../")

import circle

def test_area():
    r = 4
    area = circle.area(r)
    assert area == 50.26548245743669

def test_perimeter():
    r = 1
    perimeter = circle.perimeter(r)
    assert perimeter == 6.283185307179586


