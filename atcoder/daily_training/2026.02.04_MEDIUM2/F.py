import sys
import heapq

input = sys.stdin.readline
def solve():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    for i in range(N):
        if K == 0: break

        can_use = A[i] // X

        if can_use > 0:
            use = min(K, can_use)
            A[i] -= use * X
            K -= use
        
    if K > 0:
        A.sort(reverse=True)
        for i in range(min(N, K)):
            A[i] = 0
    print(sum(A))

if __name__ == "__main__":
    solve()