def solution(relation):
    info = dict()
    for i in range(len(relation[0])):
        info[i] = []
    for i in range(len(relation)):
        for j in range(len(relation[0])):
            

relation = [["100", "ryan", "music", "2"],
            ["200", "apeach", "math", "2"],
            ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"],
            ["500", "muzi", "music", "3"],
            ["600", "apeach", "music", "2"]]

solution(relation)
