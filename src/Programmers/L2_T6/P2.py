def solution(s):
    l = [int(i) for i in s.split()]
    result = f'{min(l)} {max(l)}'
    return result


s = '-1 2 -3 4'
print(solution(s))
