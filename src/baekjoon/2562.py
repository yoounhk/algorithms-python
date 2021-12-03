import sys

li = []
for _ in range(9):
    li.append(int(sys.stdin.readline()))

_max = max(li)
print(_max)
print(li.index(_max)+1)
