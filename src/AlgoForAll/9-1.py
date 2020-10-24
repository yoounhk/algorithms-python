l = [3, 6, 3, 2, 1, 5, 2, 2, 54, 3, 689, 45]

result = []


def find_pos(l, get):
    for i in range(len(l)):
        if get < l[i]:
            return i
    return len(l)


result = []
while l:
    get = l.pop(0)
    target_index = find_pos(result, get)
    result.insert(target_index, get)

print(result)
