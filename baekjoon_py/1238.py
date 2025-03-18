from collections import defaultdict
import heapq
import sys

def dijkstra(graph):
    distance = [INF] * (N+1)
    distance[X] = 0
    q = []
    heapq.heappush(q,(0, X))
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for next, d in graph[node].items():
            if distance[node] + d < distance[next]:
                distance[next] = distance[node] + d
                heapq.heappush(q, (distance[next], next))
    return distance


input = sys.stdin.readline
INF = 987654321
N, M, X = map(int, input().split())

graph1 = defaultdict(dict)
graph2 = defaultdict(dict)

for _ in range(M):
    A, B, T = map(int, input().split())
    graph1[A][B] = T
    graph2[B][A] = T

distance1 = dijkstra(graph1)
distance2 = dijkstra(graph2)

print(max(distance1[i] + distance2[i] for i in range(1, N+1)))