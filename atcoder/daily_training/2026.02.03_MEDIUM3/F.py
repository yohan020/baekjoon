import sys
import heapq
input = sys.stdin.readline
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_hq = []
    B_hq = []
    for i in range(N):
        heapq.heappush(A_hq, -A[i])
        heapq.heappush(B_hq, -B[i])
    print(-heapq.heappop(A_hq) - heapq.heappop(B_hq))
    

if __name__ == "__main__":
    solve()