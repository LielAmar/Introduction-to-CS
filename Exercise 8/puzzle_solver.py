from typing import List, Tuple, Set, Optional


# We define the types of a partial picture and a constraint (for type checking).
Picture = List[List[int]]
Constraint = Tuple[int, int, int]

# Constants for marking invalid, valid and partially valid return options of
# ${check_constraint}
INVALID = 0
VALID = 1
PARTIALLY_VALID = 2

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

    status = check_constraints(picture, constraints_set)
   
    print("checking picture[", row_idx, "][", col_idx, "]")
    print("picture", picture)
    print("status", status)
    print("=====")

    if status == INVALID:
        return None
    elif status == VALID:
        return picture

    if row_idx == len(picture):
        return None
    
    if col_idx == len(picture[row_idx]):
        return solve_puzzle_helper(picture, constraints_set, row_idx + 1, 0)
    
    picture[row_idx][col_idx] = 0
    res = solve_puzzle_helper(picture, constraints_set, row_idx, col_idx + 1)
    if res != None:
        return res

    picture[row_idx][col_idx] = 1
    res = solve_puzzle_helper(picture, constraints_set, row_idx, col_idx + 1)
    if res != None:
        return res

    picture[row_idx][col_idx] = -1
    return None


print()

# board = [[0] * 4 for _ in range(3)]
# print(board)


def how_many_solutions(constraints_set: Set[Constraint], n: int, m: int) -> int:
    ...


def generate_puzzle(picture: Picture) -> Set[Constraint]:
    ...
