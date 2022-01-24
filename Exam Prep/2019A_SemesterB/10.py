# Solution:
#   

class A:
    def __init__(self):
        self.x = 1

        A.y = 10

    def f(self):
        self.y += 10
    
    def __repr__(self):
        return str(A.y + self.x)

a = A()
a.f()

b = A()
b.y = 30

print(a)
print(b)