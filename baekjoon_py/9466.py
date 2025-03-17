import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start):
    global count
    visited[start] = True
    cycle.append(start)
    next = wanted[start]

    if visited[next]:
        if next in cycle:
            count -= len(cycle[cycle.index(next):])
        return
    else:
        dfs(next)

T = int(input())
for _ in range(T):
    n = int(input())
    wanted = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    count = n

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(count)