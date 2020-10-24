total = 0
max = 0
for i in range(4):
    _out, _in = input().split()
    _out = int(_out)
    _in = int(_in)
    total -= _out
    total += _in
    if total > max:
        max = total
print(max)
