import string

s = 'aaa\t\nasdasdas asdsad'
whitespaces = string.whitespace
result = ''
index = 0
for i in s:
    if i not in whitespaces:
        if index % 2 == 0:
            result += i.upper()
        else:
            result += i.lower()
        index += 1
    else:
        result += i
        index = 0

print(result)
