# 병합 정렬
list = [3, 2, 10, 11, 25, 1, 5, 178, 200, 174]


def merge_sort(list):
    # print(list)
    # 분할
    if len(list) <= 1:
        return list
    center = len(list) // 2
    left = merge_sort(list[:center])
    right = merge_sort(list[center:])
    print(f'left: {left}, right: {right}')
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    print(f'result: {result}')
    return result


merge_sort(list)
