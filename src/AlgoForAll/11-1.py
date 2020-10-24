def bubble_sort(l):
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l


print(bubble_sort([3, 2, 1, 4, 1, 23, 6, 56, 4, 31232]))
