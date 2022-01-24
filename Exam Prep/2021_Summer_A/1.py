# k=1: 0 + 1 + 0 = 1
# k=2: 1 + 1 + 1 = 3
# k=3: 3 + 1 + 3 = 7
# k=4: 4 + 3 + 1 + 3 + 4 = 15
# k=5: 8 + 4 + 3 + 1 + 3 + 4 + 8 = 31


def f(k):
    if k > 0:
        yield from f(k-1)
        yield k
        yield from f(k-1)

print(len(list(f(1))))
print(len(list(f(2))))
print(len(list(f(3))))
print(len(list(f(4))))
print(len(list(f(5))))

# An = 2*A(n-1) + 1
# 
# 

# res = 2**n - 1