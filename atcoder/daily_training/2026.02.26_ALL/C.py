import sys

input = sys.stdin.readline
def solve():
    A, B, K = map(int, input().split())
    ans = 0
    while True:
        if A >= B:
            print(ans)
            return
        A *= K
        ans += 1


if __name__ == "__main__":
    solve()