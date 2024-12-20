import square
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


def test_area():
    r = 2
    area = square.area(r)
    assert area == 4


def test_perimeter():
    r = 1
    perimeter = square.perimeter(r)
    assert perimeter == 4
