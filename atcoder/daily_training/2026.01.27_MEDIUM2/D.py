import sys

input = sys.stdin.readline
def solve():
    N, A = map(int, input().split())
    T = list(map(int, input().split()))

    ans = T[0]
    for i in range(1, N):
        ans += A
        print(ans)
        if ans < T[i]:
            ans = T[i]
    print(ans + A)

if __name__ == "__main__":
    solve()