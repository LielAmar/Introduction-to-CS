# assuming max_weight and each item is an Integer (>= 1)
def easy_knapsack(items: list[tuple[int, float]], max_weight: int) -> int:
    return knapsack_helper(items, max_weight, 0, 0, 0)
    
def knapsack_helper(items: list[tuple[int, float]],
        max_weight: int, i: int, weight: int, value: int):
    if weight > max_weight:
        return 0
    
    if i == len(items):
        return value

    value_with_item = knapsack_helper(items, max_weight, i + 1,
            weight + items[i][0], value + items[i][1])
    
    value_without_index = knapsack_helper(items, max_weight, i + 1, weight, value)
    
    return max(value_with_item, value_without_index)