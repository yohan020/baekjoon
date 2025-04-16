import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

dir = [(-1,0),(1,0),(0,-1),(0,1)]

def dfs(x, y):
    if dp[y][x]: return dp[y][x]
    dp[y][x] = 1
    for (n_y, n_x) in dir:
        temp_x = x + n_x
        temp_y = y + n_y
        if temp_x < 0 or n <= temp_x or temp_y < 0 or n <= temp_y: continue
        if bamboo[temp_y][temp_x] <= bamboo[y][x]: continue
        dp[y][x] = max(dp[y][x], dfs(temp_x, temp_y) + 1)
    return dp[y][x]

n = int(input())
bamboo = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
result = 0
for i in range(n):
    for j in range(n):
        result = max(dfs(j, i), result)
print(result)