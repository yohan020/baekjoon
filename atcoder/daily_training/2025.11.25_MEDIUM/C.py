import sys

input = sys.stdin.readline

def solve():
    H, W = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]
    for i1 in range(H):
        for i2 in range(i1, H):
            for j1 in range(W):
                for j2 in range(j1, W):
                    if grid[i1][j1] + grid[i2][j2] > grid[i2][j1] + grid[i1][j2]:
                        print("No")
                        return
    print("Yes")
    return
if __name__ == "__main__":
    solve()