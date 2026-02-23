import sys
from math import sqrt

input = sys.stdin.readline
def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    pos = []
    for _ in range(N):
        x, y = map(int, input().split())
        pos.append((x, y))

    ans = -float('inf')
    for i in range(N):
        if i + 1 in A:
            continue
        min_dist = float('inf')
        x, y = pos[i]
        for a in A:
            ax, ay = pos[a - 1]
            dist = sqrt((x - ax) ** 2 + (y - ay) ** 2)
            min_dist = min(min_dist, dist)
        ans = max(ans, min_dist)
    print(ans)



if __name__ == "__main__":
    solve()