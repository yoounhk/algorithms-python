while True:
    line = [int(i) for i in input().split()]
    if line[0] == 0:
        break
    branch = 1
    for i in range(1, len(line), 2):
        branch = branch * line[i] - line[i + 1]
    print(branch)
