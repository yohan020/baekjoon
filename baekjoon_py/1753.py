from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write

graph = defaultdict(dict)
V, E = map(int, input().split())
start = int(input())

for _ in range(E):
    flag = True
    u, v, w = map(int, input().split())
    if v in graph[u]: #graph[u]딕셔너리에 v도착노드로된 키가 있는지 확인
        if w < graph[u][v]: #있으면 거리 비교해서 더 짧으면 갱신
            graph[u][v] = w
    else: #키가 없다면 새로 추가
        graph[u][v] = w

INF = 987654321
distance = [INF] * (V + 1)
distance[start] = 0
pq = [] #우선 순위 큐를 위한 리스트 선언
heapq.heappush(pq, (0, start)) #우선 순위 큐: 첫번째 요소를 기준으로 최소값을 항상 루트로 유지하기 때문에 
#가장 짧은 거리를 가진 정점을 빠르게 찾을 수 있다.

while pq:
    cur_dist, cur_node = heapq.heappop(pq) 
    if cur_dist > distance[cur_node]: #팝한 노드까지의 거리가 기존 거리보다 길면 패스한다.
        continue
    for nxt, weight in graph[cur_node].items(): #팝한 간선의 목적지와 거리를 변수에 담으면서 거리를 갱신할지 판단한다.
        if cur_dist + weight < distance[nxt]:
            distance[nxt] = cur_dist + weight
            heapq.heappush(pq, (distance[nxt], nxt)) #만약 인접한 노드의 거리가 기존에 기록된 거리보다 짧게 계산된다면 새롭게
            # 갱신하고 우선순위큐에 넣어서 거리를 다시 갱신해준다.

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF\n")
    else:
        print(str(distance[i])+"\n")