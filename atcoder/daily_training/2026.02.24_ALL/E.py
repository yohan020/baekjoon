import sys

input = sys.stdin.readline
def solve():
    N = int(input())
    A = [0] + list(map(int, input().split()))

    same_count = 0
    ans = 0

    for i in range(1, N + 1):
        if A[i] == i:
            same_count += 1
        elif A[i] > i:
            j = A[i]
            if A[j] == i:
                ans += 1
    ans += same_count * (same_count - 1) // 2
    print(ans)


if __name__ == "__main__":
    solve()