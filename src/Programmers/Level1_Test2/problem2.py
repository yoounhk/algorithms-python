def solution(a, b):
    big = max(a, b)
    small = min(a, b)
    l = [small + i for i in range(big - small + 1)]
    return sum(l)
