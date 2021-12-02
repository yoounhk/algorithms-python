import sys

P, K = map(int, input().split())

is_prime_list = [True] * K

_max = int(K ** 0.5)

for i in range(2, _max+1):
    if is_prime_list[i] == True:
        for j in range(i+i, K, i):
            is_prime_list[j] = False

primes = [i for i in range(2, K) if is_prime_list[i] == True]

for i in primes:
    if P % i == 0:
        print(f'BAD {i}')
        sys.exit(0)
print('GOOD')
