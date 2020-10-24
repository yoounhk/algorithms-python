input = [int(i) for i in input().split()]

answer = 0
for i in input:
    answer += i ** 2
answer %= 10
print(answer)
