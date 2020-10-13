# 중위 순회
# 전위 순회
# 후위 순회

list = ['가', '나', '다', '라', '마', '바', '사', '아']


def tree(list):
    if len(list) <= 1:
        return list
    left = []
    right = []
    root = [[list.pop(0)], left, right]
    for i in list:
        if i < root[0]:
            left.append(i)
            return tree(left)
        else:
            right.append(i)
            return tree(right)
