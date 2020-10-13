# 선택 정렬

list = [4,3,2,1]
sorted_list = []
while list:
    sorted_list.append(list.pop(list.index(min(list))))
    print(list)
    print(sorted_list)
    print('----------')

print('---최종---')
print(sorted_list)
