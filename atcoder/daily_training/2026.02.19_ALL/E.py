import sys
from itertools import permutations

input = sys.stdin.readline
def solve():
    N, M = map(int, input().split())

    takahashi = [[False] * N for _ in range(N)]
    aoki = [[False] * N for _ in range(N)]

    for _ in range(M):
        u, v = map(int, input().split())
        takahashi[u - 1][v - 1] = True
        takahashi[v - 1][u - 1] = True
    for _ in range(M):
        u, v = map(int, input().split())
        aoki[u - 1][v - 1] = True
        aoki[v - 1][u - 1] = True
    
    for p in permutations(range(N)):
        is_same = True

        for i in range(N):
            for j in range(N):
                if takahashi[i][j] != aoki[p[i]][p[j]]:
                    is_same = False
                    break
            if not is_same:
                break
        if is_same:
            print("Yes")
            return
    print("No")

if __name__ == "__main__":
    solve()