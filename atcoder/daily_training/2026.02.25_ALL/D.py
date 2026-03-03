import sys

input = sys.stdin.readline
def solve():
    H, W = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]
    ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = [[] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 0:
                res[i].append('.')
            else:
                res[i].append(ABC[grid[i][j] - 1])
    for i in range(H):
        print(''.join(res[i]))
                

if __name__ == "__main__":
    solve()