# 최대공약수 구하기

a = 6
b = 12

gcd = min(a, b)

while gcd > 1:
    if a % gcd == 0 and b % gcd == 0:
        break
    gcd -= 1
print(gcd)
