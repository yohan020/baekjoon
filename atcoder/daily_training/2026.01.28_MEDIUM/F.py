import sys

input = sys.stdin.readline
def solve():
    N, M = map(int, input().split())
    S = list(map(str, input().split()))
    T = set(map(str, input().split()))
    for s in S:
        if s in T:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    solve()