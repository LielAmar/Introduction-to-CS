# Solution:

class Boss():
    def __init__(self, name):
        self.name = name

a = Boss("Iosi")
b = Boss("Ety")

b.fast = False
c = b
c.old = True
d = c
c = a
d.age = 42

print(a.__dict__)
print(b.__dict__)
print(c.__dict__)
print(d.__dict__)
