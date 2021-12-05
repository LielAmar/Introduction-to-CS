from typing import List, Tuple, Set, Optional

# We define the types of a partial picture and a constraint (for type checking).
Picture = List[List[int]]
Constraint = Tuple[int, int, int]

# ===== CONSTANTS ===== #
# Constants for marking invalid, valid and partially valid return options of
# ${check_constraint}
INVALID = 0
VALID = 1
PARTIALLY_VALID = 2

# ===== UTILS ===== #
def is_finished_picture(picture: Picture) -> bool:
    for i in range(len(picture)):
        for j in range(len(picture[i])):
            if picture[i][j] == -1:
                return False
    
    return True


def max_seen_cells(picture: Picture, row: int, col: int) -> int:
    return seen_cells_helper(picture, row, col, {-1, 1})

def min_seen_cells(picture: Picture, row: int, col: int) -> int:
    return seen_cells_helper(picture, row, col, {1})

def seen_cells_helper(picture: Picture, row: int,
        col: int, see_through: set = {-1, 1}) -> int:
    """
    A helper function to loop over all cells above & below, and left & right of
    the given cell's index. If the looped cell is a see-through, we want to add
    1 to the count, otherwise we break the loop.
    """

    if not picture[row][col] in see_through:
        return 0

    # Setting the initial value of result to 1 since we know
    # picture[row][col] is a see-through
    result = 1

    for i in range(row - 1, -1, -1):
        if not picture[i][col] in see_through: break
        result += 1

    for i in range(row + 1, len(picture), 1):
        if not picture[i][col] in see_through: break
        result += 1

    for j in range(col - 1, -1, -1):
        if not picture[row][j] in see_through: break
        result += 1
     
    for j in range(col + 1, len(picture[row]), 1):
        if not picture[row][j] in see_through: break
        result += 1

    return result


def check_constraints(picture: Picture, constraints_set: Set[Constraint]) -> int:
    """
    Checks all given constraints in ${constaints_set} and returns whether they
    are all valid, partially valid or invalid.
    """

    imperfect_constraints = 0

    for constraint in constraints_set:
        row, col, seen = constraint
        
        max_seen = max_seen_cells(picture, row, col)
        min_seen = min_seen_cells(picture, row, col)

        if max_seen < seen or seen < min_seen:
            return INVALID
        elif min_seen == seen == max_seen:
            continue
        elif min_seen <= seen <= max_seen:
            imperfect_constraints += 1
    
    if imperfect_constraints != 0:
        return PARTIALLY_VALID
    
    return VALID


def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) -> Optional[Picture]:
    picture: Picture = [[-1] * m for _ in range(n)]

    return solve_puzzle_helper(picture, constraints_set, 0, 0)

def solve_puzzle_helper(picture: Picture, constraints_set: Set[Constraint],
        row_idx: int, col_idx: int) -> Optional[Picture]:
    """
    Uses backtracing to find a solution to ${picture}, taking ${constraints_set}
    in account.
    
    If we reach a dead-end, meaning the status of our picutre is INVALID, we can
    automatically drop it.
    If we get a VALID status, we found a solution and we want to return it.
    Otherwise, we keep on looking and testing different values for each cell,
    and always advance our indexes
    """

    status = check_constraints(picture, constraints_set)

    # Checks the status of the current picture
    if status == INVALID:
        return None
    elif status == VALID:
        return picture

    # If we reached the end of the row/rows, we want to quit/move on to the next row
    if row_idx == len(picture):
        return None
    elif col_idx == len(picture[row_idx]):
        return solve_puzzle_helper(picture, constraints_set, row_idx + 1, 0)
    
    # Backtracing with the values of {0, 1} in our current index
    # If we got a solution we want to stop and return it
    for value in range(0, 2):
        picture[row_idx][col_idx] = value
        res = solve_puzzle_helper(picture, constraints_set, row_idx, col_idx + 1)

        if res != None: return res

    # revert our changes and go back in the recursion hierarchy
    picture[row_idx][col_idx] = -1
    return None
  

def how_many_solutions(constraints_set: Set[Constraint], n: int, m: int) -> int:
    picture: Picture = [[-1] * m for _ in range(n)]

    return how_many_solutions_helper(picture, constraints_set, 0, 0)

def how_many_solutions_helper(picture: Picture, constraints_set: Set[Constraint],
        row_idx: int, col_idx: int) -> int:
    """
    Uses backtracing to find the number of solutions to ${picture}, taking ${constraints_set}
    in account.
    
    If we reach a dead-end, meaning the status of our picutre is INVALID, we can
    automatically drop it and return 0.
    If we get a VALID status (and the picutre is finished, meaning all entries
    are either 0 or 1), we found a solution and we want to return 1 to stack up.
    Otherwise, we keep on looking and testing different values for each cell,
    and always advance our indexes
    """

    status = check_constraints(picture, constraints_set)

    res = 0

    # Checks the status of the current picture
    if status == INVALID:
        return 0
    elif status == VALID and is_finished_picture(picture):
        return 1

    # If we reached the end of the row/rows, we want to quit/move on to the next row
    if row_idx == len(picture):
        return 0
    elif col_idx == len(picture[row_idx]):
        return res + how_many_solutions_helper(picture, constraints_set, row_idx + 1, 0)


    # Backtracing with the values of {0, 1} in our current index
    # If we got a solution we want to stop and return it
    for value in range(0, 2):
        picture[row_idx][col_idx] = value
        res += how_many_solutions_helper(picture, constraints_set, row_idx, col_idx + 1)

    # revert our changes and go back in the recursion hierarchy
    picture[row_idx][col_idx] = -1
    return res


def generate_puzzle(picture: Picture) -> Set[Constraint]:
    constraints_set: Set[Constraint] = set()
    
    for i in range(len(picture)):
        for j in range(len(picture[i])):
            constraints_set.add((i, j, max_seen_cells(picture, i, j)))

    return generate_puzzle_helper(picture, constraints_set)

def generate_puzzle_helper(picture: Picture,
        constraints_set: Set[Constraint]) -> Optional[Set[Constraint]]:

    number_of_solutions = how_many_solutions(constraints_set,
            len(picture), len(picture[0]))

    solution = constraints_set

    for constraint in constraints_set:
        cloned: Set[Constraint] = set(constraints_set)
        cloned.remove(constraint)

        suspected_solution = generate_puzzle_helper(picture, cloned)
        if suspected_solution != None:
            solution = suspected_solution

    if number_of_solutions == 1:
        return solution

    return None