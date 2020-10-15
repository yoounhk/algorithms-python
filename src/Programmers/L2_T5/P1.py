def solution(s):
    if len(s) == 0:
        return 1
    elif len(s) == 1:
        return 0
    else:
        for i in range(1, len(s)):
            prev = s[i - 1]
            if s[i] == prev and i + 1 < len(s):
                return solution(s[:i - 1] + s[i + 1:])
            elif s[i] == prev and i + 1 == len(s):
                return solution(s[:i - 1])
        return 0


print(solution('cbb'))
print(solution('abc'))
print(solution('bcb'))
