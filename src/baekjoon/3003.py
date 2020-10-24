chess = [1, 1, 2, 2, 2, 8]
input = [int(i) for i in input().split()]
answer = [str(chess[i] - input[i]) for i in range(len(chess))]
print(' '.join(answer))
