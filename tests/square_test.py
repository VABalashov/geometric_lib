import sys

sys.path.append("../")

import square

def test_area():
    r = 2
    area = square.area(r)
    assert area == 4

def test_perimeter():
    r = 1
    perimeter = square.perimeter(r)
    assert perimeter == 4


