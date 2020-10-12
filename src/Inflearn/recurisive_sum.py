# 재귀 함수로 리스트 전체 합 구하기
def sum(n):
    if len(n) == 1:
        return n[0]
    else:
        return n[0] + sum(n[1:])

print(sum([1,2,3,4]))