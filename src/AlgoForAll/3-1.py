# n명 중 두명을 뽑아 짝을 지을 수 있는 조합을 모두 출력하기
def solution(names):
    names = list(set(names))
    for i in range(len(names) - 1):
        for j in range(i + 1, len(names)):
            print(f'{names[i]} - {names[j]}')


names = ['김철수', '김영희', '김철수', '김철수', '김철수', '김영희', '이민수', '이민수']

solution(names)
