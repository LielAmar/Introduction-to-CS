from tkinter import N
from turtle import pos


def all_sums(num, bound):
    possiblities = []

    find_all_possibilities(num, bound, possiblities, [])

    for lst in possiblities:
        yield " + ".join(lst)

def find_all_possibilities(num, bound, possibilities, path):
    if num == 0:
        if not contains(possibilities, path):
            possibilities.append(path)
            return
    
    if num < 0:
        return

    for i in range(1, bound+1):
        find_all_possibilities(num-i, bound, possibilities, [str(i)] + path)
    
    return

def contains(big_list, small_list):
    small_srtd = sorted(small_list)

    for inner_list in big_list:
        if len(inner_list) != len(small_list): continue

        srtd = sorted(inner_list)

        matched = True
        for i in range(len(srtd)):
            if srtd[i] != small_srtd[i]:
                matched = False
                break
                
        if matched:
            return True

    return False


res = all_sums(4, 3)
print(list(res))

if __name__ == "__main__":
    assert len(list(all_sums(10, 5))) == len(['5 + 5', '5 + 4 + 1', '5 + 3 + 2', '5 + 3 + 1 + 1', '5 + 2 + 2 + 1', '5 + 2 + 1 + 1 + 1', '5 + 1 + 1 + 1 + 1 + 1', '4 + 4 + 2', '4 + 4 + 1 + 1', '4 + 3 + 3', '4 + 3 + 2 + 1', '4 + 3 + 1 + 1 + 1', '4 + 2 + 2 + 2', '4 + 2 + 2 + 1 + 1', '4 + 2 + 1 + 1 + 1 + 1', '4 + 1 + 1 + 1 + 1 + 1 + 1', '3 + 3 + 3 + 1', '3 + 3 + 2 + 2',
                                     '3 + 3 + 2 + 1 + 1', '3 + 3 + 1 + 1 + 1 + 1', '3 + 2 + 2 + 2 + 1', '3 + 2 + 2 + 1 + 1 + 1', '3 + 2 + 1 + 1 + 1 + 1 + 1', '3 + 1 + 1 + 1 + 1 + 1 + 1 + 1', '2 + 2 + 2 + 2 + 2', '2 + 2 + 2 + 2 + 1 + 1', '2 + 2 + 2 + 1 + 1 + 1 + 1', '2 + 2 + 1 + 1 + 1 + 1 + 1 + 1', '2 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1', '1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1'])