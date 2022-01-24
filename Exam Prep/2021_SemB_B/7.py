def f7(f, g):
    g(f)

def func1(x):
    return x + 7

def func2(x):
    return x

final = f7(func1, func2)
final = func1

result = f7(-5)

# 2