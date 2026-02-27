import sys
from collections import deque

input = sys.stdin.readline
def solve():
    H, W = map(int, input().split())
    S = [list(input().rstrip()) for _ in range(H)]
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                continue
            ans += 1
            queue = deque([(i, j)])
            S[i][j] = '.'
            while queue:
                x, y = queue.popleft()
                for dx, dy in dir:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == '#':
                        S[nx][ny] = '.'
                        queue.append((nx, ny))
    print(ans)
if __name__ == "__main__":
    solve()