"""
눈 떠보니 코테 1번 문제
섬으로 향하라!

'   + -- + - + -   '
'   + --- + - +   '
'   + -- + - + -   '
'   + - + - + - +   '

해(1)와 달(0),
Code의 세상 안으로!(En-Coding)
"""
item = ['   + -- + - + -   ',
        '   + --- + - +   ',
        '   + -- + - + -   ',
        '   + - + - + - +   ']
result = []
for i in item:
    result.append(chr(int(i.lstrip().rstrip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)))
print(''.join(result))
