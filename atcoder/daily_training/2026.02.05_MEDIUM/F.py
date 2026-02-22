import sys
from bisect import bisect_right

input = sys.stdin.readline
def solve(N:int, A:list):
    A_unique = list(set(A))
    A_unique.sort()
    K = [0] * N
    for a in A:
        idx = bisect_right(A_unique, a)
        K[len(A_unique) - idx] += 1
    print("\n".join(map(str, K)))
    

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    solve(N, A)