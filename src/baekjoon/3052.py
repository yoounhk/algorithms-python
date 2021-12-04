li = []
for _ in range(10):
    li.append(int(input()) % 42)
s = set(li)
print(len(s))
