import sys

n = int(input())

if n == 1:
    print(1)
    sys.exit(0)

adder = 1
level = 1

while adder < n:
    adder = adder + (6*level)
    level += 1

print(level)
