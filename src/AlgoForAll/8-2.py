# 선택 정렬 내림차로 구현

l = [4, 3, 6, 1, 12, 45, 123]
for i in range(len(l) - 1):
    max_idx = i
    for j in range(i + 1, len(l)):
        if l[j] > max_idx:
            max_idx = j
        l[i], l[max_idx] = l[max_idx], l[i]

print(l)
