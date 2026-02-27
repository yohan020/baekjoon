import sys
from collections import deque

input = sys.stdin.readline
def solve():
    H, W = map(int, input().split())
    grid = [input().rstrip() for _ in range(H)]
    dir = [(0, 1), (1, 0)]

    visited = [[False] * W for _ in range(H)]
    visited[0][0] = True

    max_depth = 0
    dq = deque([(0, 0, 1)])  # (row, col, depth)

    while dq:
        r, c, depth = dq.popleft()
        max_depth = max(max_depth, depth)
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == '.' and not visited[nr][nc]:
                visited[nr][nc] = True
                dq.append((nr, nc, depth + 1))
    
    print(max_depth)
if __name__ == "__main__":
    solve()