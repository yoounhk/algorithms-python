import time

total = 0
for i in range(4):
    total += int(input())

t = time.localtime(total)
print(f'{t.tm_min}\n{t.tm_sec}')
