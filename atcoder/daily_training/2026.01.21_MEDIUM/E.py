import sys

input = sys.stdin.readline
def solve():
    N = int(input())
    domino = list(map(int, input().split()))
    ans = 0
    e = 0
    for i in range(0, N):
        e = max(e, domino[i])
        ans += 1
        e -= 1
        if e == 0:
            print(ans)
            return
    print(ans)

if __name__ == "__main__":
    solve()