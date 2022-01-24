def lexico_iter(lst):
    size = 0
    
    while True:
        yield from lexico_helper(lst, size)
        
        size += 1
    

def lexico_helper(lst, size):
    if size <= 0:
        yield ""
        return
        
    for char in lst:
        for item in lexico_helper(lst, size-1):
            yield char + item

if __name__ == "__main__":
    res = lexico_iter(["a"])
    assert(next(res) == "" and next(res) == "a" and next(res) == "aa" and next(res) == "aaa")
    
    res = lexico_iter(["a", "b"])
    assert(next(res) == "" and next(res) == "a" and next(res) == "b" and next(res) == "aa" \
            and next(res) == "ab" and next(res) == "ba" and next(res) == "bb" and next(res) == "aaa")
            
    res = lexico_iter(["a", "b", "c"])
    assert(next(res) == "" and next(res) == "a" and next(res) == "b" and next(res) == "c" \
            and next(res) == "aa" and next(res) == "ab" and next(res) == "ac")