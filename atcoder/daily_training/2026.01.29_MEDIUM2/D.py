import sys
import heapq

input = sys.stdin.readline
def solve():
    Q = int(input())
    hq = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            heapq.heappush(hq, x)
        elif query[0] == 2:
            if hq:
                print(heapq.heappop(hq))


if __name__ == "__main__":
    solve()