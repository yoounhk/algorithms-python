import string
import collections

s = input()

alphabets = list(string.ascii_lowercase)
_dict = dict()
for char in alphabets:
    _dict[char] = -1
for index, char in enumerate(s):
    if _dict[char] == -1:
        _dict[char] = index
    elif _dict[char] != -1:
        pass

for i in _dict.values():
    print(f'{i}', end=' ')
