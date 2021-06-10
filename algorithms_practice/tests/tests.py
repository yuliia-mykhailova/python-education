import pytest

from algorithms_practice.algorithms.algorithms import *


# binary_search()
@pytest.mark.parametrize('test_arg, expected',
                         [(([1, 2, 3, 4, 5, 6, 7, 8, 9], 4), 3),
                          (([0, 1, 2, 2, 2, 3, 4, 5, 6], 2), 4),
                          (([-4, -3, -2, -1, 0, 1, 2, 3, 4], -2), 2),
                          (([0, 1, 2, 3, 4, 5, 7, 8, 9], 6), -1)])
def test_binary_search(test_arg, expected):
    assert binary_search(*test_arg) == expected


# quick_sort()
@pytest.mark.parametrize('test_arg, expected',
                         [([1, 1], [1, 1]),
                          ([1], [1]),
                          ([2, 3, 1, 0, 2, 3, 0, 1], [0, 0, 1, 1, 2, 2, 3, 3]),
                          ([-2, -3, -1, 0, 2, 3, 0, 1], [-3, -2, -1, 0, 0, 1, 2, 3])])
def test_quick_sort(test_arg, expected):
    assert quick_sort(test_arg) == expected


# factorial()
@pytest.mark.parametrize('test_arg, expected',
                         [(0, 1),
                          (1, 1),
                          (5, 120)])
def test_factorial(test_arg, expected):
    assert factorial(test_arg) == expected
