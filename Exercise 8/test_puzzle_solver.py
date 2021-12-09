from puzzle_solver import *

def test_max_seen_cells_func():
    picture = [[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]]

    assert max_seen_cells(picture, 0, 0) == 1
    assert max_seen_cells(picture, 1, 0) == 0
    assert max_seen_cells(picture, 1, 2) == 5
    assert max_seen_cells(picture, 1, 1) == 3

def test_min_seen_cells_func():
    picture = [[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]]

    assert min_seen_cells(picture, 0, 0) == 0
    assert min_seen_cells(picture, 1, 0) == 0
    assert min_seen_cells(picture, 1, 2) == 0
    assert min_seen_cells(picture, 1, 1) == 1

def test_check_constraints_func():
    picture1 = [[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]]
    picture2 = [[0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 0]]

    assert check_constraints(picture1, {(0, 3, 5), (1, 2, 5), (2, 0, 1)}) == 0
    assert check_constraints(picture2, {(0, 3, 3), (1, 2, 5), (2, 0, 1)}) == 1
    assert check_constraints(picture1, {(0, 3, 3), (1, 2, 5), (2, 0, 1)}) == 2

def test_solve_puzzle_func():
    assert solve_puzzle({(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 0)}, 3, 4) == [[0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    assert solve_puzzle({(0, 3, 3), (1, 2, 5), (2, 0, 1), (2, 3, 5)}, 3, 4) == None
    assert solve_puzzle({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3) in [[[0, 0, 1], [1, 1, 1], [1, 1, 1]] or [[1, 0, 1], [1, 1, 1], [1, 1, 1]]]

def test_how_many_solutions_func():
    assert how_many_solutions({(0, 3, 3), (1, 2, 5), (2, 0, 1), (2, 3, 5)}, 3, 4) == 0
    assert how_many_solutions({(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 1)}, 3, 4) == 1
    assert how_many_solutions({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3) == 2
    assert how_many_solutions({(i, j, 0) for i in range(3) for j in range(3)}, 3, 3) == 1
    assert how_many_solutions(set(), 2, 2) == 16
    assert how_many_solutions({(0, 3, 3), (2, 0, 1)}, 3, 4) == 64

def test_generate_puzzle_func():
    picture = [[1, 0, 0], [1, 1, 1]] 

    solution = generate_puzzle(picture)

    allowed = [
        {(0, 0, 2), (1, 2, 3)},
        {(1, 0, 4), (0, 1, 0), (0, 2, 0)},
        {(1, 0, 4), (0, 0, 2), (0, 2, 0)},
        {(1, 0, 4), (1, 1, 3), (0, 2, 0)},
        {(1, 0, 4), (1, 1, 3), (1, 2, 3)},
        {(1, 0, 4), (0, 1, 0), (1, 2, 3)},
        {(0, 0, 2), (1, 1, 3), (0, 1, 0), (0, 2, 0)}
    ]

    assert solution in allowed


def dont_test_generate_ALL_solutions():
    def generate_all_puzzle(picture: Picture) -> Set[Constraint]:
        constraints_set: List[Constraint] = list()
    
        for i in range(len(picture)):
            for j in range(len(picture[i])):
                constraints_set.append((i, j, max_seen_cells(picture, i, j)))

        return generate_all_puzzle_helper(picture, constraints_set)

    def generate_all_puzzle_helper(picture: Picture,
            constraints_set: List[Constraint]) -> Optional[List[Constraint]]:

        number_of_solutions = how_many_solutions(constraints_set,
                len(picture), len(picture[0]))

        solution = constraints_set

        import random

        random.shuffle(constraints_set)

        for constraint in constraints_set:
            cloned: List[Constraint] = list(constraints_set)
            cloned.remove(constraint)

            suspected_solution = generate_all_puzzle_helper(picture, cloned)
            if suspected_solution != None:
                solution = suspected_solution

        if number_of_solutions == 1:
            return solution

        return None

    solutions = list()
    for _ in range(70):
        print(_)
        sol = generate_all_puzzle([[1, 0, 0], [1, 1, 1]])
        sol.sort()
        if not sol == solutions:
            solutions.append(sol)
    
    solutions.sort()
    solutions_set = set(tuple(x) for x in solutions)
    solutions = list(map(list, solutions_set))

    assert solutions == [[(0, 0, 2), (0, 1, 0), (0, 2, 0), (1, 1, 3)], [(0, 0, 2), (0, 2, 0), (1, 0, 4)], [(1, 0, 4), (1, 1, 3), (1, 2, 3)], [(0, 0, 2), (1, 2, 3)], [(0, 2, 0), (1, 0, 4), (1, 1, 3)], [(0, 1, 0), (1, 0, 4), (1, 2, 3)], [(0, 1, 0), (0, 2, 0), (1, 0, 4)]]