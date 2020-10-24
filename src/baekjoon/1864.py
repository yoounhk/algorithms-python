while True:
    line = input()
    if line == '#':
        break
    out = 0
    for i in range(len(line)):
        if line[i] == '-':
            tmp = 0
        elif line[i] == '\\':
            tmp = 1
        elif line[i] == '(':
            tmp = 2
        elif line[i] == '@':
            tmp = 3
        elif line[i] == '?':
            tmp = 4
        elif line[i] == '>':
            tmp = 5
        elif line[i] == '&':
            tmp = 6
        elif line[i] == '%':
            tmp = 7
        elif line[i] == '/':
            tmp = -1
        out += tmp * (8 ** (len(line) - i - 1))
    print(out)
