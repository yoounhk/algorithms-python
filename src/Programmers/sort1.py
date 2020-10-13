array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    result = []
    for i in commands:
        arr = array[i[0] - 1:i[1]]
        arr.sort()
        result.append(arr[i[2] - 1])
    return result


print(solution(array, commands))
