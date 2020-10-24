names = ['김', '이', '박', '최', '김']

d = dict()

for i in names:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print([i for i in d if d[i] > 1])
