from power_set import *
from knapsack import *
from n_queens import *

def test_power_set():
    assert power_set([1,2,3]) == [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
    assert power_set([]) == [[]]
    assert power_set([1]) == [[], [1]]


def test_knapsacking():
    items = [
        (1, 1.0),
        (4, 2.0),
        (3, 5.0)
    ]
    assert easy_knapsack(items, 5) == 6.0


def test_place_queens():
    assert place_queens(8) == True