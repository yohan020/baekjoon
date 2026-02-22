import sys

input = sys.stdin.readline
def solve(degree: list, N: int) -> None:
    for i in range(1, N + 1):
        if degree[i] == N - 1:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    N = int(input())
    degree = [0] * (N + 1)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        degree[a] += 1
        degree[b] += 1
    solve(degree, N)