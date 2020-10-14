def solution(n):
    binary = bin(n)[2:]
    targetOne = numberOfOne(binary)
    while True:
        n += 1
        if targetOne == numberOfOne(bin(n)[2:]):
            return n


def numberOfOne(str):
    sum = 0
    for i in str:
        if i == '1':
            sum += 1
    return sum


n = 1
