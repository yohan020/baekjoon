import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    books = list(map(int, input().split()))
    dp = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]
    sum = [0] * (N+1)
    for i in range(1, N+1):
        sum[i] = sum[i-1] + books[i-1]
    for i in range(1, N+1): dp[i][i] = 0

    for L in range(2, N+1):
        for i in range(1, N - L + 2):
            j = i + L - 1
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + (sum[j] - sum[i-1])
                dp[i][j] = min(dp[i][j], cost)
    print(dp[1][N])