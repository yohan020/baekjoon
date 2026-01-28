import sys

input = sys.stdin.readline
def solve():
    s = [str(input().strip()) for _ in range(3)]
    t = str(input().strip())

    for i in t:
        print(s[int(i)-1], end='')


if __name__ == "__main__":
    solve()