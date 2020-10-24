# https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    column_stack = [list() for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                column_stack[j].append(board[i][j])
    target_stack = []
    for i in range(len(moves)):
        if column_stack[moves[i] - 1][0] != 0:
            target_stack.append(column_stack[moves.pop(i) - 1].pop(0))
            break
    if len(target_stack) == 0:
        return 0
    popped = 0
    for i in range(len(moves)):
        if column_stack[moves[i] - 1]:
            if target_stack[-1] != column_stack[moves[i] - 1][0]:
                target_stack.append(column_stack[moves[i] - 1].pop(0))
            else:
                popped += 2
    print(target_stack)
    return popped


board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board, moves))
