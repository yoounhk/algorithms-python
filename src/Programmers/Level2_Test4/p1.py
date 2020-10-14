def solution(board):
    max = 0
    if len(board) < 2 or len(board[0]) < 2:
        for i in board:
            for j in i:
                if j == 1:
                    return 1
        return 0
    for i in range(1,len(board)):
        for j in range(1,len(board[i])):
            ul = board[i-1][j-1]
            l = board[i][j-1]
            u = board[i-1][j]
            if ul > 0 and l > 0 and u > 0 and board[i][j] == 1:
                board[i][j] += min(ul,l,u)
            if board[i][j] > max:
                max = board[i][j]
    return max*max
