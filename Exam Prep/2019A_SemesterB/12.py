def describe_str(st1):
    if len(st1) == 0: return ""

    char = st1[0]
    amount = same_char_helper(st1, 0)

    return char + str(amount) + describe_str(st1[amount:])

def same_char_helper(s, k):
    char = s[k]
    
    count = 0
    for i in range(k, len(s)):
        if s[i] == char:
            count += 1
        else:
            break
    
    return count

if __name__ == "__main__":
    print(describe_str("abbcccdeaa"))

    print(same_char_helper("aabbbcccccdd", 0))
    print(same_char_helper("aabbbcccccdd", 4))
    print(same_char_helper("aabbbcccccdd", 5))
