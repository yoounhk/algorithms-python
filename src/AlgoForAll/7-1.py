# 리스트에서 찾는 값을 찾아 인덱스로 돌려주기

l = [1, 1, 1, 2, 3, 4]

target = 1

result = []
for i in range(len(l)):
    if l[i] == 1:
        result.append(i)

print(result)
