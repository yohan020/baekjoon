import sys

input = sys.stdin.readline
def solve():
    A, B = map(int, input().split())
    C = (A**2 + B**2)**0.5
    n = 1 / C
    print(A * n, B * n)

if __name__ == "__main__":
    solve()