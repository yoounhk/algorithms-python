import sys

T = int(input())

for _ in range(T):
    score, streak = 0, 0
    _input = sys.stdin.readline().rstrip()
    for i in _input:
        if i == 'O':
            streak += 1
            score += streak
        elif i == 'X':
            streak = 0
    print(score)
