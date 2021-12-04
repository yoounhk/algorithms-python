import sys

T = int(input())

for _ in range(T):
    n, s = sys.stdin.readline().split()
    print("".join(list(map(lambda x: x * int(n), s))))
