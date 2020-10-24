while True:
    num = [i for i in input()]
    if num[0] == '0':
        break
    cm = 1
    for i in num:
        if i == '0':
            cm += 4
        elif i == '1':
            cm += 2
        else:
            cm += 3
        cm += 1
    print(cm)
