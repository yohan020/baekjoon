import sys
import math

input = sys.stdin.readline

def solve():
    D = int(input())

    ans = D 
    limit = math.isqrt(D) + 2

    for x in range(limit):
        x2 = x * x

        rem = D - x2
        if rem < 0:
            diff = abs(rem)
            ans = min(ans, diff)
            break
            
        y = math.isqrt(rem)

        val1 = abs(x2 + y * y - D)
        ans = min(ans, val1)

        val2 = abs(x2 + (y + 1) * (y + 1) - D)
        ans = min(ans, val2)

    print(ans)

if __name__ == "__main__":
    solve()