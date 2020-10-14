def count(str):
    sum = 0
    for i in str:
        if i == '1':
            sum += 1
    return sum


def solution(n):
    i = n + 1
    while True:
        if count(bin(n)[2:]) == count(bin(i)[2:]):
            return i
        i += 1
