import sys
from itertools import permutations

input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    adj = [[False] * N for _ in range(N)]

    for _ in range(M):
        u, v = map(int, input().split())
        adj[u-1][v-1] = True
        adj[v-1][u-1] = True
    max_overlap = 0

    def count_edge(path):
        cnt = 0
        L = len(path)
        for i in range(L):
            u = path[i]
            v = path[-1]
            if adj[u][v]:
                cnt += 1
        return cnt
    
    for p in permutations(range(N)):
        current_overlap = count_edge(p)
        if current_overlap > max_overlap:
            max_overlap = current_overlap
        
        for d in range(3, N - 2):
            cycle1 = p[:d]
            cycle2 = p[d:]
            
            overlap2 = count_edge(cycle1) + count_edge(cycle2)
            if overlap2 > max_overlap:
                max_overlap = overlap2
    ans = M + N - 2 * max_overlap
    print(ans)

if __name__ == "__main__":
    solve()
