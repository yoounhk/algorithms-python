# 친구 찾아서 모두 출력하기

d = {1: [2, 3],
     2: [1],
     3: [1, 4],
     4: [3]}


def getFriends(d, me):
    print(f'{me}의 친구들과 친밀도 입니다')
    q = []
    done = set()
    q.append((me, 0))
    done.add(me)
    while q:
        (person, friendPoint) = q.pop(0)
        print(f'{me}와 {person}의 친밀도는 {friendPoint}입니다')
        for i in d[person]:
            if i not in done:
                q.append((i, friendPoint + 1))
                done.add(i)


for i in range(1, len(d) + 1):
    getFriends(d, i)
