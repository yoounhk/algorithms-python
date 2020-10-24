def solution(n):
    nPerShip = [25,40,55,70,85, 100]
    hour = range(9,21)
    daysOfMonth = [2**i for i in range(10,0,-1)]
    now = '2020-01-01'

    manPerDay = len(hour) * 100
    manPerYear = manPerDay * sum(daysOfMonth)
    나머지 = n % manPerYear
    흐른년도 = n // manPerYear
    print(나머지)
    print(흐른년도)

solution(14000605)