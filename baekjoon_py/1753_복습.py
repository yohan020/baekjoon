from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write

V, E = map(int, input().split())
start = int(input())

graph = defaultdict(dict)

for _ in range(E):
    u, v, w = map(int, input().split())
    if v in graph[u]:
        if w < graph[u][v]:
            graph[u][v] = w
    else:
        graph[u][v] = w

q = []
INF = 987654321
distance = [INF] * (V+1)
distance[start] = 0
heapq.heappush(q, (0, start))

while q:
    now_dis, now = heapq.heappop(q)
    if distance[now] < now_dis:
        continue
    for next, next_dis in graph[now].items():
        if next_dis + distance[now] < distance[next]:
            distance[next] = next_dis + distance[now]
            heapq.heappush(q, (distance[next], next))

for i in distance[1:V+1]:
    if i == INF:
        print("INF\n")
    else:
        print(str(i) + "\n")