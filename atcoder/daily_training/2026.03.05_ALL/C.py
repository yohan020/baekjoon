import sys

input = sys.stdin.readline
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    left = 0
    right = 0
    for i in range(N):
        if A[i] == 1:
            left = i
            break
    for i in range(N - 1, -1, -1):
        if A[i] == 1:
            right = i
            break
    print(right - left)

if __name__ == "__main__":
    solve()