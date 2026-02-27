import sys

input = sys.stdin.readline
# def solve():
#     N = int(input())
#     sheet = []
#     max_x = 0
#     max_y = 0
#     for _ in range(N):
#         a, b, c, d = map(int, input().split())
#         sheet.append((a, b, c, d))
#         max_x = max(max_x, b)
#         max_y = max(max_y, d)
#     grid = [[0] * (max_y) for _ in range(max_x)]
#     for a, b, c, d in sheet:
#         for i in range(a, b):
#             for j in range(c, d):
#                 grid[i][j] += 1
#     ans = 0
#     for i in range(max_x):
#         for j in range(max_y):
#             if grid[i][j] > 0:
#                 ans += 1
#     print(ans)
def solve(): # 업그레이드 된 버젼 : 2차원 누적합을 이용하여 O(N + max_x * max_y)로 풀이
    N = int(input())
    grid = [[0] * 102 for _ in range(102)]

    for _ in range(N):
        a,b,c,d = map(int, input().split())
        grid[a][c] += 1
        grid[b][d] += 1
        grid[a][d] -= 1
        grid[b][c] -= 1
    
    for i in range(101):
        for j in range(1, 101):
            grid[i][j] += grid[i][j-1]
    for j in range(101):
        for i in range(1, 101):
            grid[i][j] += grid[i-1][j]
    ans = 0
    for i in range(101):
        for j in range(101):
            if grid[i][j] > 0:
                ans += 1
    print(ans)
    

if __name__ == "__main__":
    solve()