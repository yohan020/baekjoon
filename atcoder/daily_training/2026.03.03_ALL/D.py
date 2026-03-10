import sys

input = sys.stdin.readline
def solve():
    N = input().strip()
    l_n = len(N)
    if l_n < 4:
        print(N)
    elif l_n < 5:
        print(N[:3] + "0")
    elif l_n < 6:
        print(N[:3] + "00")
    elif l_n < 7:
        print(N[:3] + "000")
    elif l_n < 8:
        print(N[:3] + "0000")
    elif l_n < 9:
        print(N[:3] + "00000")
    elif l_n < 10:
        print(N[:3] + "000000")
    return

if __name__ == "__main__":
    solve()