class ReverseEnumerateIterator:
    def __init__(self, string):
        self.x = [(string[i], i) for i in range(len(string))]

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.x:
            raise StopIteration
        return self.x.pop()