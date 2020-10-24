def quick_sort(l):
    if len(l) <= 1:
        return l

    pivot = l.pop(0)
    left = []
    right = []
    while l:
        if l[0] < pivot:
            left.append(l.pop(0))
        else:
            right.append(l.pop(0))
    return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort([3, 2, 1]))
