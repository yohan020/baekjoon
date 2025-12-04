import sys

input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    S = set(A)

    for i in range(K):
        if i not in S:
            print(i)
            return
    print(K)

if __name__ == "__main__":
    solve()