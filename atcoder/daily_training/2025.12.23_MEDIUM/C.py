import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    grid = [[0] * 100 for _ in range(100)]
    for _ in range(N):
        A, B, C, D = map(int, input().split())
        for i in range(A, B):
            for j in range(C, D):
                grid[i][j] = 1
    print(sum(map(sum, grid)))
        
if __name__ == "__main__":
    solve()