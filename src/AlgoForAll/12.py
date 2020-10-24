def binary_search(l, target):
    if len(l) == 1:
        return 1 if target == l[0] else 0
    mid = len(l) // 2
    if target == l[mid]:
        return 1
    elif target < l[mid]:
        return binary_search(l[:mid], target)
    elif target > l[mid]:
        return binary_search(l[mid:], target)


l = [1, 2, 3, 4, 5]

print(binary_search(l, 5))
