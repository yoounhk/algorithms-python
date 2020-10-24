num = [39, 14, 67, 105]
name = ['J', 'K', 'M', 'S']
d = {}
for i in range(len(num)):
    d[num[i]] = name[i]
target = 39
print(d[target] if target in d else '?')
