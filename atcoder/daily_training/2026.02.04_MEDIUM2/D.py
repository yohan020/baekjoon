import sys

input = sys.stdin.readline
def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    num = 1
    for a in A:
        num *= a
        if (K + 1) <= len(str(num)):
            num = 1
    print(num)
    

if __name__ == "__main__":
    solve()