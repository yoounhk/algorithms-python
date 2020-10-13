# 퀵 소트
list = [13,50,22,10,593,120,204,123]

def quick_sort(list):
    if len(list) <= 1:
        return list
    pivot = list.pop(0)
    left = []
    right = []
    for i in list:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(list))