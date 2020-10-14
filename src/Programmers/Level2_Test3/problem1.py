import collections


def 소인수분해(n):
    seed = 2
    l = []
    while n >= seed:
        if n % seed == 0:
            l.append(seed)
            n //= seed
        else:
            seed += 1
    return l


def solution(arr):
    dic = dict()
    for i in arr:
        l = 소인수분해(i)
        l = collections.Counter(l)
        for i in l:
            if i not in dic:
                dic[i] = l[i]
            dic[i] = max(dic[i], l[i])
    result = 1
    for i in dic:
        result *= i ** dic[i]
    return result


arr = [6, 8, 12]

print(solution(arr))
