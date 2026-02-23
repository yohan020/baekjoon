import sys

input = sys.stdin.readline
def solve():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(1, n):
        if A[i-1] + 1 != A[i]:
            print(A[i-1] + 1)
            return


if __name__ == "__main__":
    solve()