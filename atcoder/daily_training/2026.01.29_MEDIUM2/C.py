import sys

input = sys.stdin.readline
def solve():
    a, b, c, d, e, f = map(int, input().split())
    g, h, i, j, k, l = map(int, input().split())

    if (g < d and a < j) and (h < e and b < k) and (i < f and c < l):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()