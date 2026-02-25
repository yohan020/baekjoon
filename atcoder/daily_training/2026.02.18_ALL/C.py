import sys

input = sys.stdin.readline
def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = [0] * M
    for i in range(N):
        cnt[A[i] - 1] += 1
        if 0 not in cnt:
            print(N - i)
            return
    print(0)

if __name__ == "__main__":
    solve()