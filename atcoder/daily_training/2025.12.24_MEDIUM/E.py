import sys
from string import ascii_lowercase

input = sys.stdin.readline

def solve():
    N = int(input())
    S = input()
    Q = int(input())
    mapping_from = 'abcdefghijklmnopqrstuvwxyz'
    mapping_to = 'abcdefghijklmnopqrstuvwxyz'
    for _ in range(Q):
        c, d = map(str, input().split())
        mapping_to = mapping_to.replace(c, d)
    for i in range(N):
        idx = mapping_from.index(S[i])
        print(mapping_to[idx], end='')
if __name__ == "__main__":
    solve()