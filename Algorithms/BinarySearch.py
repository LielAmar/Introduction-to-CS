def binary_sort(item, sequence):
    return binary_sort_helper(item, sequence, 0, len(sequence))

def binary_sort_helper(item, sequence, low, high):
    if high <= low:
        return -1
    
    mid = (low + high) // 2
    if item == sequence[mid]:
        return mid 
    elif item > sequence[mid]:
        return binary_sort_helper(item, sequence, mid+1, high)
    else:
        return binary_sort_helper(item, sequence, low, mid)