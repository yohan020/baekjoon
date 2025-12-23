import sys
import heapq

input = sys.stdin.readline

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    hq = []
    for a in A:
        heapq.heappush(hq, -a)
    heapq.heappop(hq)
    target = -hq[0]
    print(A.index(target)+1)
    

if __name__ == "__main__":
    solve()