import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())

    if M != N - 1:
        print("No")
        return

    degree = [0] * (N + 1)
    adj = [[] for _ in range(N + 1)]

    for _ in range(M):
        u, v = map(int, input().split())
        degree[u] += 1
        degree[v] += 1
        adj[u].append(v)
        adj[v].append(u)

    count_1 = 0
    for i in range(1, N + 1):
        if degree[i] > 2: 
            print("No")
            return
        if degree[i] == 1:
            count_1 += 1
    
    if count_1 != 2:
        print("No")
        return

    visited = [False] * (N + 1)
    
    # DFS 함수
    def dfs(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs(v)

    dfs(1)

    if sum(visited) != N:
        print("No") 
        return

    print("Yes")

if __name__ == "__main__":
    solve()