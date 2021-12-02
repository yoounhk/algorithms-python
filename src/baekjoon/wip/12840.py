import sys
h, m, s = map(int, input().split())
Q = int(input())

now = h*3600 + m*60 + s

for _ in range(Q):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 3:
        print(f"{now // 3600} {(now % 3600) // 60} {now % 60}")
    else:
        T, seconds = query[0], query[1]
        if T == 1:
            now = (now + seconds) % 86400
        elif T == 2:
            if now - seconds < 0:
                now += 86400
            now -= seconds
            # now = (now - seconds) % 86400
