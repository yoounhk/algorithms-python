# https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3#
# 1번 수포자 1,2,3,4,5
def one(n):
    list = [5, 1, 2, 3, 4]
    return list[n % 5]


# 2번 수포자 2, 1, 2, 3, 2 , 4, 2 ,5
def two(n):
    list = [5, 1, 3, 4]
    if n % 2 == 1:
        return 2
    else:
        return list[(n // 2) % 4]


# 3번 수포자 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
def three(n):
    list = [5, 3, 1, 2, 4]
    return list[((n + 1) // 2) % 5]


def solution(answers):  # max length 10000
    score = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == one(i + 1):
            score[0] += 1
        if answers[i] == two(i + 1):
            score[1] += 1
        if answers[i] == three(i + 1):
            score[2] += 1
    maximum = max(score)
    result = []
    for i in range(len(score)):
        if score[i] == maximum:
            result.append(i + 1)
    return result
