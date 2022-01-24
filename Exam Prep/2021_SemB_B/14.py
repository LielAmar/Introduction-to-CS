def guess_pass(pwd, text):
    if not pwd:
        return []
        
    if not text:
        return False

    found = ""
    for i, char in enumerate(text):
        if char in pwd and found.count(char) < pwd.count(char) and char == pwd[len(found)]:
            found += char
    
    if found != pwd:
        return False
        
    index = text.index(pwd[0])
    res = guess_pass(pwd[1:], text[index+1:])
    rest = []
    
    if res:
        rest = [i+(index+1) for i in res]
        
    return [index] + rest

if __name__ == "__main__":
    pwd="abc-123"
    text="abc-123abc-123"
    assert guess_pass(pwd, text) == [0, 1, 2, 3, 4, 5, 6]
    pwd = "abc-123"
    text= "a1b2c34/-1x2gh3n"
    print(guess_pass(pwd, text))
    assert guess_pass(pwd, text) == [0, 2, 4, 8, 9, 11, 14]
    pwd = "abc-123"
    text = "acb-123"
    assert guess_pass(pwd, text) == False
    pwd = ""
    text = "abcd"
    assert guess_pass(pwd, text) == []
    pwd = "a"
    text = ""
    assert guess_pass(pwd, text) == False
    pwd = ""
    text = ""
    assert guess_pass(pwd, text) == []