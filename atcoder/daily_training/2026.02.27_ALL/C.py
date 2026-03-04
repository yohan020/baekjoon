import sys

input = sys.stdin.readline
def solve():
    A = list(map(int, input().split()))
    ans = 0
    for i in range(len(A)):
        ans += A[i] * 2 ** i
    print(ans)

if __name__ == "__main__":
    solve()