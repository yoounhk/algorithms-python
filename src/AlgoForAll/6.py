# 하노이의 탑 옮기기
import math


def printNumber(n, max):
    digit = int(math.log10(max) + 1)

    print(f'{n:{digit}d}' * n)


def printBlank(n, max):
    pass


def printTower(n):
    for i in range(1, n + 1):
        printNumber(i, n)


def hanoi(n, start, aux, end):
    printTower(n)
    # if (n == 1):
    #     print(' '*7+str(n))
    #     print('ㅁ--ㅁ--ㅁ')
    # hanoi(n-1, aux, end, start)


hanoi(10, 1, 1, 1)
