def solution(n):
    result = []
    for i in range(1, n):
        if i % 3 == 1:
            result.append(1)
        elif i % 3 == 2:
            result.append(2)
        elif i % 3 == 0:
            result.append(3)
    return result


for i in range(1, 10):
    print(solution(i))
