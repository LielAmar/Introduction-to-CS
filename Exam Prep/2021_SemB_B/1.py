# Solution:
#     x=23, y=4253
#     x != y
#     x !> y
#     x % 10 == 3 & y % 10 == 3 ->
#  f1(2, 425)
#    x=2, y=425
#    x != y
#    x !> y
#    x % 10 == 2 & y % 10 == 5 ->
#  f1(2, 42)
#    x=2, y=42
#    x != y
#    x !> y
#    x % 10 == 2 & y % 10 == 2 ->
#  f1(0, 4)
#    x=0, y=4
#    x != y
#    x !> y
#    x % 10 == 0 & y % 10 == 4 ->
#  f1(0, 0)
#    return True
#
#  [True]

def f1(x, y):
    if x == y:
        return True
    if x > y:
        return False
    if x % 10 == y % 10:
        return f1(x//10, y//10)
    else:
        return f1(x, y//10)

print(list(map(f1,[23],(4253,))))