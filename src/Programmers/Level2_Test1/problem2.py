def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i] >= l - i:
            return l - i
    return 0


n = [0, 1, 3, 5, 6]

print(solution(n))
