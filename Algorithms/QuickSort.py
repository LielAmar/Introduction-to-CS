import random

def partition(sequence: list, start: int, end: int) -> int:
    pivot_index = start
    pivot = sequence[pivot_index]

    while start < end:
        while start < len(sequence) and sequence[start] <= pivot:
            start += 1

        while sequence[end] > pivot:
            end -= 1

        if start < end:
            sequence[start], sequence[end] = sequence[end], sequence[start]
    
    sequence[end], sequence[pivot_index] = sequence[pivot_index], sequence[end]
    return end


def quick_sort(sequence, start, end):
    if start < end:
        pivot_index = partition(sequence, start, end)

        quick_sort(sequence, start, pivot_index - 1)
        quick_sort(sequence, pivot_index + 1, end)

if __name__ == "__main__":
    sequence = [3, 8, 1, 0, 5, 9, 2, 6, 7]
    
    quick_sort(sequence, 0, len(sequence) - 1)
    
    print(sequence)