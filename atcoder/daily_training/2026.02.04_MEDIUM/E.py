import sys
from bisect import bisect_right, bisect_left

input = sys.stdin.readline

def solve(N, M, A, B):
    A.sort()
    B.sort()
    low = 1
    ans = 0
    high = 10**9 + 1
    while low <= high:
        mid = (low + high) // 2
        # bisect_right는 mid 보다 첫 큰 위치를 반환
        seller_cnt = bisect_right(A, mid)
        # bisect_left는 mid 보다 크거나 같은 첫 위치
        buyer_cnt = M - bisect_left(B, mid)

        if seller_cnt >= buyer_cnt:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

        
    

if __name__ == "__main__":
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(solve(N, M, A, B))