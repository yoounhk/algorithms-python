def solution(names):
    same_names = set()
    for i in range(len(names) - 1):
        for j in range(i + 1, len(names)):
            if names[i] == names[j]:
                same_names.add(names[i])
    return same_names


names = ['김철수', '김영희', '김철수', '김철수', '김철수', '김영희', '이민수', '이민수']

print(solution(names))
