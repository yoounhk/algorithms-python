# 숫자 n 개중에 최댓값 찾기 재귀 함수
def f(l):
    if len(l) == 1:
        return l[0]
    if l[0] > l[1]:
        l.pop(1)
        return f(l)
    else:
        l.pop(0)
        return f(l)


print(f([1, 2, 3, 3, 23, 123, 123, 1111]))
