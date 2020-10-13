numbers = [2, 1, 3, 4, 1]


def solution(numbers):
    subs = []
    for i in range(len(numbers)):
        current = numbers[i]
        ex = numbers[:i] + numbers[i + 1:]
        while ex:
            subs.append(current + ex.pop(0))
            print(subs)
    result = list(set(subs))
    result.sort()
    return result


print(solution(numbers))
