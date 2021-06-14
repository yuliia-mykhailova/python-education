from random import randint
from math import factorial as fact

import pytest

from algorithms_practice.algorithms.algorithms import *


# binary_search()
@pytest.fixture()
def test_array():
    """Returns random array"""
    array = []
    for i in range(5):
        array.append(randint(0, 20))
    return array


def test_binary_search(test_array):
    test_array = sorted(test_array)
    rand_int = randint(0, len(test_array))
    assert binary_search(test_array, test_array[rand_int]) == rand_int


# quick_sort()
def test_quick_sort(test_array):
    assert quick_sort(test_array) == sorted(test_array)


# factorial()
def test_factorial():
    for i in range(5):
        rand_int = randint(0, 10)
        assert factorial(rand_int) == fact(rand_int)
