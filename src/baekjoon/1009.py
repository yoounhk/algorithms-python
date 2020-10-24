t = int(input())
table = [
    [10],
    [1],
    [2, 4, 8, 6],
    [3, 9, 7, 1],
    [4, 6],
    [5],
    [6],
    [7, 9, 3, 1],
    [8, 4, 2, 6],
    [9, 1]
]
for i in range(t):
    a, b = map(int, input().split())
    a = int(str(a)[-1])
    print(table[a][(b - 1) % len(table[a])])
