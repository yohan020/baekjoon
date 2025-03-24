import math

X, Y, D, T = map(int, input().split())

d = math.sqrt(X**2 + Y**2)

ans = d

if d < D:
    ans = min(ans, T + (D - d), 2 * T)
else:
    n = int(d // D)  
    r = d - n * D   
    candidate1 = n * T + r
    candidate2 = (n + 1) * T
    ans = min(ans, candidate1, candidate2)

print(float(ans))
