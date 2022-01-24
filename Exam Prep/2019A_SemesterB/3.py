# Solution:
#   5
#     i = 10
#     a = [1] 
#     a = [1, 2]
#   5
#   [1, 2]
#     a = [1, 2, 3]
#   10
#   [1,2,3]

n = 20
def f(n):
    print(n)
    i = 10
    a = [1]
    a.append(2)
    def f_inner():
        print(n)
        print(a)
        i = 11
        a.append(3)
    f_inner()
    print(i)
    print(a)

f(5)