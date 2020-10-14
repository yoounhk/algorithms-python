def solution(record):
    l = []
    dic = dict()
    for i in record:
        splited = i.split()
        l.append([splited[0], splited[1]])
        if splited[0] == 'Enter':
            dic[splited[1]] = splited[2]
        elif splited[0] == 'Change':
            dic[splited[1]] = splited[2]
    result = []
    for status, id in l:
        if status == 'Enter':
            result.append(dic[id] + '님이 ' + '들어왔습니다.')
        elif status == 'Leave':
            result.append(dic[id] + '님이 ' + '나갔습니다.')
    return result


record = ["Enter uid1234 Muzi",
          "Enter uid4567 Prodo",
          "Leave uid1234",
          "Enter uid1234 Prodo",
          "Change uid4567 Ryan"]

solution(record)
