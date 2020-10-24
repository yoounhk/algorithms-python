q = []
s = []

str = 'abcdcba'

for i in str:
    if i.isalpha():
        q.append(i)
        s.append(i)

while q:
    if q.pop(0) != s.pop():
        print(f'{str}은 회문이 아니다')
        break

    if len(q) == 0:
        print(f'{str}은 회문이다')
