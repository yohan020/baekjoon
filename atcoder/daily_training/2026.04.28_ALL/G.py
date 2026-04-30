import sys
from collections import defaultdict

input = sys.stdin.readline
def solve():
    H, W, N = map(int, input().split())
    trash_x = defaultdict(int)
    trash_y = defaultdict(int)
    
    row_to_cols = defaultdict(list)
    col_to_rows = defaultdict(list)

    alive = set()

    for _ in range(N):
        a, b = map(int, input().split())
        a -= 1
        b -= 1

        trash_x[a] += 1
        trash_y[b] += 1

        row_to_cols[a].append(b)
        col_to_rows[b].append(a)

        alive.add((a, b))
    
    Q = int(input())

    for _ in range(Q):
        t, v = map(int, input().split())
        v -= 1

        if t == 1:
            print(trash_x[v])

            for y in row_to_cols[v]:
                if (v, y) in alive:
                    alive.remove((v, y))
                    trash_y[y] -= 1
            trash_x[v] = 0
            row_to_cols[v] = []
        else:
            print(trash_y[v])

            for x in col_to_rows[v]:
                if (x, v) in alive:
                    alive.remove((x, v))
                    trash_x[x] -= 1
            trash_y[v] = 0
            col_to_rows[v] = []

        

if __name__ == "__main__":
    solve()