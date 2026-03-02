import sys
from collections import deque

input = sys.stdin.readline
def solve():
    N = int(input())
    win = []
    for i in range(N):
        S = input().rstrip()
        w = S.count('o')
        win.append((i+1, w))
    win.sort(key=lambda x: (x[1], -x[0]), reverse=True)
    for i in range(N):
        print(win[i][0], end=' ')

if __name__ == "__main__":
    solve()