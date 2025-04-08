import sys
input = sys.stdin.readline

N = int(input())

primes = [True] * (N+1)

primes[0] = False
primes[1] = False

for i in range(2, int(N** 0.5) + 1):
    if primes[i]:
        for j in range(i*2, N+1, i):
            primes[j] = False

primes = [i for i in range(2, N+1) if primes[i]]

i = 0
j = 0
l = len(primes)
total = 0
cnt = 0

while True:
    if total == N:
        cnt += 1
    if total > N:
        total -= primes[i]
        i += 1
    elif j == l:
        break
    else:
        total += primes[j]
        j += 1
print(cnt)