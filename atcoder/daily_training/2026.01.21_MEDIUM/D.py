import sys

input = sys.stdin.readline


        


def solve():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    adj_mat = [[False] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        adj_mat[a][b] = True
        adj_mat[b][a] = True
    
    global_count = 0

    def dfs(curr, start, depth):
        if depth == 2:
            if adj_mat[curr][start]:
                return 1
            return 0
        cnt = 0

        for neighbor in graph[curr]:
            if neighbor > curr:
                cnt += dfs(neighbor, start, depth + 1)
        return cnt
    
    for i in range(1, N + 1):
        global_count += dfs(i, i, 0)
    
    print(global_count)

        


if __name__ == "__main__":
    solve()