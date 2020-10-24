# 그래프 탐색하기

g = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}


def graph_searh(g, start):
    q = []
    done = set()

    q.append(start)
    done.add(start)
    while q:
        print(f'현재 큐: {q}')
        print(f'현재 완료 대상: {list(done)}')
        target = q.pop(0)
        print(f'{target}을 기준으로 탐색을 시작합니다.')
        for i in g[target]:
            if i not in done:
                done.add(i)
                q.append(i)


graph_searh(g, 1)
