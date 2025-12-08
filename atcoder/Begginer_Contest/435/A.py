import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    print(sum([i for i in range(1, N+1)]))
if __name__ == "__main__":
    solve()