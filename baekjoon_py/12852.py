import sys

def solve(N):
    dp = [0] * (N + 1)
    prev = [0] * (N + 1)
    dp[1] = 0
    for i in range(2, N+1):
        dp[i] = dp[i - 1] + 1
        prev[i] = i - 1
        if i % 3 == 0 and dp[i//3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1
            prev[i] = i // 3
        if i % 2 == 0 and dp[i//2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            prev[i] = i // 2
    print(dp[N])
    
    path = []
    while N != 0:
        path.append(N)
        N = prev[N]
    sys.stdout.write(" ".join(map(str, path)))


N = int(input())
solve(N)