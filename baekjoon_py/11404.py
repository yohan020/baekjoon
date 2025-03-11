import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[987654321] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for i in range(1, n+1):
    graph[i][i] == 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (i == j): continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    res = []
    for j in range(1, n+1):
        if graph[i][j] == 987654321:
            res.append("0")
        else:
            res.append(str(graph[i][j]))
    print(" ".join(res))