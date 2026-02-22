import sys

input = sys.stdin.readline
def solve():
    N, M = map(int, input().split())
    A = set(map(int, input().split()))

    cnt = 0
    arr = []
    for i in range(1, N + 1):
        if i not in A:
            cnt += 1
            arr.append(i)
    print(cnt)
    print(*arr)

if __name__ == "__main__":
    solve()