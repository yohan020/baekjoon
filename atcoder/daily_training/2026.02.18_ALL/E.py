import sys

input = sys.stdin.readline
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    arr = [0] * N
    res = []
    for a in A:
        arr[a - 1] += 1
        if arr[a - 1] == 2:
            res.append(a)
    print(*res)

if __name__ == "__main__":
    solve()