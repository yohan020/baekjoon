import sys

input = sys.stdin.readline

def solve():
    H, W, N = map(int, input().split())
    T = input().strip()
    grid = []
    gnd = []
    
    grid = [input().strip() for _ in range(H)]

    candidates = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.':
                candidates.append((i, j))
    
    moves = {
        'L': (0, -1),
        'R': (0, 1),
        'U': (-1, 0),
        'D': (1, 0)
    }

    for cmd in T:
        dx, dy = moves[cmd]
        next_candidates = []
        for r, c in candidates:
            nr, nc = r + dx, c + dy
            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == '.':
                next_candidates.append((nr, nc))
        candidates = next_candidates

        if not candidates:
            break
    print(len(candidates))


if __name__ == "__main__":
    solve()