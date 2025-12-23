import sys


def solve():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    visited = [False] * (N+1)
    max_dist = 0

    def dfs(u, current_dist):
        nonlocal max_dist
        if current_dist > max_dist:
            max_dist = current_dist
        visited[u] = True
        for v, w in graph[u]:
            if not visited[v]:
                dfs(v, current_dist + w)
        visited[u] = False
    
    for i in range(1, N+1):
        dfs(i, 0)
    
    print(max_dist)
    

if __name__ == "__main__":
    solve()