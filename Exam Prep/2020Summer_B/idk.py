def tree(data, subtrs=[]): return [data] + list(subtrs)
def data(t): return t[0]
def subtrs(t): return t[1:]
def leaf(t): return not subtrs(t)

def bound_track_max(tree, bound):
    if bound <= 0:
        return []

    return bound_track_helper(tree, bound, [])

def bound_track_helper(tree, bound, current_path):
    parent_data = [data(tree)]
    current_path += parent_data

    if leaf(tree):
        return current_path

    max_sol = current_path

    if len(max_sol) > bound:
        max_sol = []
    
    for child in subtrs(tree):
        if len(current_path) < bound:
            child_sol_w_parent = bound_track_helper(child, bound, current_path[:])

            if sum(child_sol_w_parent) > sum(max_sol) and len(child_sol_w_parent) <= bound:
                max_sol = child_sol_w_parent

        child_sol_wout_parent = bound_track_helper(child, bound, [])

        if sum(child_sol_wout_parent) > sum(max_sol) and len(child_sol_wout_parent) <= bound:
            max_sol = child_sol_wout_parent

    return max_sol


if __name__ == "__main__":
    tr1 = tree(4, [tree(3, [tree(8), tree(2)]), tree(7, [tree(5, [tree(6), tree(1)])])])
    tr2 = tree(2, [tree(3, [tree(5), tree(6)]), tree(7)])
    tr3 = tree(2, [tree(3, [tree(5), tree(6, [tr1])]), tree(7)])

    assert bound_track_max(tr1, 1) == [8]
    assert bound_track_max(tr1, 2) == [7, 5]
    assert bound_track_max(tr1, 3) == [7, 5, 6]
    assert bound_track_max(tr1, 4) == [4, 7, 5, 6]
    assert bound_track_max(tr1, 5) == [4, 7, 5, 6]

    assert bound_track_max(tr2, 1) == [7]
    assert bound_track_max(tr2, 2) in [[3, 6], [2, 7]]
    assert bound_track_max(tr3, 8) == [2, 3, 6, 4, 7, 5, 6]
    print("all test has passed!")