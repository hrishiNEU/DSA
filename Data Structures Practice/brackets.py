def isValid(s: str) -> bool:
    compliments = {"(":")","[":"]","{":"}"}

    s_len = len(s)

    if s_len % 2 != 0:
        return False

    half_len = s_len // 2

    for i in range(half_len):
        comp_char = s[i]
        comp_bracket = compliments[comp_char]
        if s[(s_len - i) - 1] != comp_bracket:
            return False

    return True 

some = isValid("()[]{}")
print(some)