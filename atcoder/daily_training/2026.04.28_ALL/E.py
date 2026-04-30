import sys
import math as m

input = sys.stdin.readline
def solve():
    N = int(input())
    res = ""
    while (N > 0):
        if (N % 2 == 1):
            res += "A"
            N = N - 1
        else:
            res += "B"
            N //= 2
    print(res[::-1])
    

if __name__ == "__main__":
    solve()