import sys

a = int(input())
b = int(input())
c = int(input())

abc = str(a*b*c)
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
result_list = [0] * 10

i = 0
for digit in digits:
    result_list[i] = abc.count(digit)
    i += 1

for item in result_list:
    print(item)
