import calculate
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


def test_valid():
    assert calculate.calc('circle', 'area', [5])


def test_invalid():
    try:
        calculate.calc('cube', 'area', [5])
    except AssertionError:
        assert True

    try:
        calculate.calc('circle', 'length', [5])
    except AssertionError:
        assert True

    try:
        calculate.calc('circle', 'area', '1')
    except AssertionError:
        assert True


def test_funcValid():
    assert calculate.calc('triangle', 'perimeter', [1, 1, 1]) == 3
