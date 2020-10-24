l, p = input().split()
l = int(l)
p = int(p)

inputs = [int(i) for i in input().split()]

for i in inputs:
    print(i - l * p, end=' ')
