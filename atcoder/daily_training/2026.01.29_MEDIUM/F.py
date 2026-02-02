import sys

input = sys.stdin.readline
def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for _ in range(Q):
        x = int(input())
        left = 0
        right = N
        while left < right:
            mid = (left + right) // 2
            if A[mid] < x:
                left = mid + 1
            else:
                right = mid
        print(N - left)

if __name__ == "__main__":
    solve()