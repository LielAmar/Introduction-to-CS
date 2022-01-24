class Interval:
    def __init__(self, x, y):
        self.a = min(x, y)
        self.b = max(x, y)
    
    def __str__(self):
        return "[" + str(self.a) + "," + str(self.b) + "]"
        
    
    def contains_zero(self):
        return self.a <= 0 and self.b >= 0
    
    
    def __add__(self, other):
        operations = []
        
        for one in self:
            for two in other:
                operations.append(one + two)
        
        return Interval(min(operations), max(operations))
        
    def __sub__(self, other):
        operations = []
        
        for one in self:
            for two in other:
                operations.append(one - two)
        
        return Interval(min(operations), max(operations))
        
    def __mul__(self, other):
        operations = []
        
        for one in self:
            for two in other:
                operations.append(one * two)
        
        return Interval(min(operations), max(operations))
        
    def __truediv__(self, other):
        if other.contains_zero():
            raise ValueError(str(other) + " contains 0, so it can not be used")
    
        operations = []
        
        for one in self:
            for two in other:
                operations.append(one / two)
        
        return Interval(min(operations), max(operations))
        
    
    def __iter__(self):
        yield self.a
        yield self.b
        

if __name__ == "__main__":
    inty = Interval(2,4)
    inty1 = Interval(3,1)
    inty2 = Interval(-1,2)
    inty3 = Interval(4,4)
    inty4 = Interval(0,0)
    
    try:
        inty/inty2
        assert False
    except:
        assert True
        
    res = inty/(inty3+inty2)
    assert res.a == 1/3 and res.b == 4/3
    
    res = inty3-inty2
    assert res.a == 2 and res.b == 5
    
    res = inty*inty3
    assert res.a == 8 and res.b == 16
    
    res = inty*inty3-inty2
    assert res.a == 6 and res.b == 17
    
    res = inty*(inty3-inty2)
    assert res.a == 4 and res.b == 20