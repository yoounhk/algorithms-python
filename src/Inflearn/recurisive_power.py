# 재귀함수로 제곱 구하

def f(n, e):
    if e == 1:
        return n
    else:
        return n*f(n,e-1)


print(f(2,7))