import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    folder = {}
    for _ in range(N):
        s = input().strip()
        if s not in folder:
            folder[s] = 0
            print(s)
        else:
            folder[s] += 1
            print(s+f'({folder[s]})')

if __name__ == "__main__":
    solve()