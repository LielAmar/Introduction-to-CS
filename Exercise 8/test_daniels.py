from puzzle_solver import *


def test_max_Seen_cells():
    picture = [[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]]
    assert max_seen_cells(picture, 0, 0) == 1
    assert max_seen_cells(picture, 1, 0) == 0
    assert max_seen_cells(picture, 1, 2) == 5
    assert max_seen_cells(picture, 1, 1) == 3


def test_min_Seen_cells():
    picture = [[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]]
    assert min_seen_cells(picture, 1, 0) == 0
    assert min_seen_cells(picture, 1, 2) == 0
    assert min_seen_cells(picture, 0, 0) == 0
    assert min_seen_cells(picture, 1, 1) == 1


def test_check_constraints():
    picture1 = [[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]]
    picture2 = [[0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 0]]

    assert check_constraints(picture1, {(0, 3, 5), (1, 2, 5), (2, 0, 1)}) == 0
    assert check_constraints(picture2, {(0, 3, 3), (1, 2, 5), (2, 0, 1)}) == 1
    assert check_constraints(picture1, {(0, 3, 3), (1, 2, 5), (2, 0, 1)}) == 2


def test_solve_puzzle():
    assert solve_puzzle({(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 0)}, 3, 4) == [
        [0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    assert solve_puzzle(
        {(0, 3, 3), (1, 2, 5), (2, 0, 1), (2, 3, 5)}, 3, 4) == None
    pic = solve_puzzle({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3)
    pic in [[[[0, 0, 1], [1, 1, 1], [1, 1, 1]],
             [[1, 0, 1], [1, 1, 1], [1, 1, 1]]]]


def test_how_many_solutions():
    assert how_many_solutions(
        {(0, 3, 3), (1, 2, 5), (2, 0, 1), (2, 3, 5)}, 3, 4) == 0
    assert how_many_solutions(
        {(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 1)}, 3, 4) == 1
    assert how_many_solutions({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3) == 2
    assert how_many_solutions({(i, j, 0) for i in range(3)
                              for j in range(3)}, 3, 3) == 1
    assert how_many_solutions(set(), 2, 2) == 16


    # assert how_many_solutions_helper([[0, 1], [0, 1], [0, 1], [0, -1], [0, -1]], {(0, 1, 4)}, 0, 0) == 1
    assert how_many_solutions({(0, 1, 2), (0, 0, 0), (1, 0, 0), (2, 0, 0)}, 3, 2) == 1

    # Should work for any given A,B
    A = 2
    B = 3
    assert how_many_solutions(set(), A, B) == 2**(A*B)
    assert how_many_solutions({(0, 3, 3), (2, 0, 1)}, 3, 4) == 64


def test_generate_solution():
    picture = [[1, 0, 0],
               [1, 1, 1]]

    class Solution:
        def __init__(self, constraints: Set[Tuple[int, int, int]]):
            self.__constraints = constraints

        def get_constraints(self):
            return self.__constraints

        def __eq__(self, other):
            if len(self.__constraints) != len(other.__constraints):
                return False
            for con in self.__constraints:
                if con not in other.__constraints:
                    return False
            return True
    solutions = [Solution([(0, 0, 2), (1, 2, 3)]),
                 Solution([(1, 0, 4), (0, 1, 0), (0, 2, 0)]),
                 Solution([(1, 0, 4), (0, 0, 2), (0, 2, 0)]),
                 Solution([(1, 0, 4), (1, 1, 3), (0, 2, 0)]),
                 Solution([(1, 0, 4), (1, 1, 3), (1, 2, 3)]),
                 Solution([(1, 0, 4), (0, 1, 0), (1, 2, 3)]),
                 Solution([(0, 0, 2), (1, 1, 3), (0, 1, 0), (0, 2, 0)])]
    solution = Solution(generate_puzzle(picture))

    for sol in solutions:
        if solution == sol:
            break
    else:
        assert True, "The solution in not correct"

    # count = how_many_solutions(
    #     solution.get_constraints(), len(picture), len(picture[0]))
    # assert how_many_solutions(
    #     solution.get_constraints(), len(picture), len(picture[0])) == 1
