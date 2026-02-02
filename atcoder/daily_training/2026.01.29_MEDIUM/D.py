import sys

input = sys.stdin.readline
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print("Yes")
        return
    gongbi = A[1] / A[0]
    for i in range(1, N):
        if A[i] * A[0] != A[i - 1] * A[1]:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    solve()