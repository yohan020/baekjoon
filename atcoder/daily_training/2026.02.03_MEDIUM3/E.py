import sys

input = sys.stdin.readline
def solve():
    N = int(input())
    T = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        arr = list(map(int, input().split()))
        T[i] = arr[0]
        if arr[1] > 0:
            graph[i] = arr[2:]
            graph[i].sort()
    visited = [False] * (N + 1)
    stack = [N]
    total_time = 0
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        total_time += T[node]
        for neighbor in graph[node]:
            if not visited[neighbor]:
                stack.append(neighbor)
    print(total_time)
if __name__ == "__main__":
    solve()