import sys

input = sys.stdin.readline
def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    res = []
    start = 0
    for i in range(M):
        time = A[i] - start - 1
        n = 0
        while time - n >= 0:
            res.append(time - n)
            n += 1
        start = A[i]
    print('\n'.join(map(str, res)))

if __name__ == "__main__":
    solve()