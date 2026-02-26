import sys

input = sys.stdin.readline
def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    sum_A = sum(A)
    if sum_A < M:
        print("No")
        return
    m = sum_A - M
    if m in A:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()