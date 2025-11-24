import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    cost = [list(map(int, input().split())) for _ in range(N)]
    dp = [[[0,0,0] for _ in range(M)]] + [[[float('inf'), float('inf'), float('inf')] for _ in range(M)] for _ in range(N)]
    for i in range(1, N+1):
        for j in range(M):
            if j < M - 1:
                dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + cost[i-1][j]
            if j > 0:
                dp[i][j][2] = min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + cost[i-1][j]
            dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + cost[i-1][j]
    ans = float('inf')
    for i in range(M):
        ans = min(ans, min(dp[N][i]))
    print(ans)
if __name__ == "__main__":
    main()