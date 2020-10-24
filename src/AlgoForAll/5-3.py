# 재귀함수로 피보나치 수열 구하기
def fib(n):
    if n <= 1:
        return n
    return fib(n - 2) + fib(n - 1)


print(fib(5))
