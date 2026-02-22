import sys

input = sys.stdin.readline
def solve():
    N, M = map(int, input().split())

    adj = [[] for _ in range(N + 1)]
    degree = [0] * (N + 1)

    for _ in range(M):
        line = input().split()
        u = int(line[0])
        v = int(line[2])
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    circle_count = 0
    non_circle_count = 0

    visited = [False] * (N + 1)
    for i in range(1, N + 1):
        if not visited[i]:
            stack = [i]
            visited[i] = True
            component_nodes = []

            while stack:
                node = stack.pop()
                component_nodes.append(node)
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

            is_circle = True
            for node in component_nodes:
                if degree[node] != 2:
                    is_circle = False
                    break
            if is_circle:
                circle_count += 1
            else:
                non_circle_count += 1
    print(circle_count, non_circle_count)
            


if __name__ == "__main__":
    solve()