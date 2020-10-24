# 최대 공약수 구하기 유클리드 호제법
def gcd(a, b):
    big = max(a, b)
    small = min(a, b)
    if small == 0:
        return big
    return gcd(small, big % small)


print(gcd(123232, 43432))
