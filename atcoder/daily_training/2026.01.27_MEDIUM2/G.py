import sys
from itertools import combinations

input = sys.stdin.readline
def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    dp = [float('-inf')] * (M + 1)

    dp[0] = 0

    for num in A:
        for j in range(M, 0, -1):
            if dp[j - 1] != float('-inf'):
                dp[j] = max(dp[j], dp[j - 1] + j * num)
    print(dp[M])
if __name__ == "__main__":
    solve()