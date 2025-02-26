def solve(N):
    dp = [0] * (N+1)
    dp[1] = 0
    for i in range(2, N+1):
        dp[i] = dp[i-1] + 1
        if i % 2 == 0 and dp[i//2] + 1 < dp[i]:
            dp[i] = dp[i//2] + 1
        if i % 3 == 0 and dp[i//3] + 1 < dp[i]:
            dp[i] = dp[i//3] + 1
    print(dp[1: N + 1])

n = int(input())
solve(n)