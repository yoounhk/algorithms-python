s = input().split()
n = int(s[0])
m = int(s[1])
isNewbie = False
if m == 1 or m == 2:
    print('NEWBIE!')
    isNewbie = True
elif m <= n and not isNewbie:
    print('OLDBIE!')
else:
    print('TLE!')
