import sys
import heapq

input = sys.stdin.readline
def solve():
    N, K = map(int, input().split())
    pq = []
    sum_b = 0
    for _ in range(N):
        a, b = map(int, input().split())
        sum_b += b
        heapq.heappush(pq, (a, b))
    ans = 1
    while sum_b > K:
        a, b = heapq.heappop(pq)
        sum_b -= b
        ans = a + 1
    print(ans)


if __name__ == "__main__":
    solve()