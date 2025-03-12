import heapq
import sys
input = sys.stdin.readline

N = int(input())

q = []
for _ in range(N):
    heapq.heappush(q, int(input()))

result = 0
if N != 1:
    for _ in range(N-1):
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        result += a + b
        heapq.heappush(q, a+b)

print(result)