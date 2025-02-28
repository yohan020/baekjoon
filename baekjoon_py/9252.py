s1 = str(input())
s2 = str(input())
n = len(s1)
dp = [[-1] * 2 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i):
        