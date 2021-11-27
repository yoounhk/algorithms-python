
def isPalindrome(s: str) -> bool:
    _list = []
    for char in s:
        if char.isalnum():
            _list.append(char.lower())
    print(_list)

    i = 0
    j = len(_list) - 1

    half_length = len(
        _list) // 2 if len(_list) % 2 == 0 else len(_list) // 2 + 1

    for k in range(half_length):
        if _list[i] != _list[j]:
            return False
        i += 1
        j -= 1
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
