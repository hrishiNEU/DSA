import string
def isPalindrome(s: str) -> bool:
    new_s = s.replace(" ","")
    newer_s = new_s.lower()

    translator = str.maketrans('', '', string.punctuation)
    newest_s = newer_s.translate(translator)

    newer_str_len = len(newest_s)
    print(newer_str_len)
    half_len = newer_str_len // 2
    print(half_len)

    for i in range(1,half_len):
        if newest_s[i] != newest_s[newer_str_len-i]:
            return False
    
    return True
        
some = isPalindrome("ab")
print(some)