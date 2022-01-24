# from collections import Counter

# source = [1,2]
# source[1] = source

# def create(n):
#     x = [[source[:] for i in range(n)] for j in range(n)]

#     return Counter(x).values()

# print(create(10))

def f(n, m, j):
    if n<= 0 or m <= 0:
        return 1
    if j <= 1:
        return 1 + f(n-1, m, m)

    return 1 + f(n, m, j-1)

print(f(5, 5, 5)) # 26
print(f(4, 5, 5)) # 21
print(f(3, 5, 5)) # 16
print(f(3, 4, 4)) # 13
print(f(3, 3, 3)) # 10
print(f(5, 6, 6)) # 31
