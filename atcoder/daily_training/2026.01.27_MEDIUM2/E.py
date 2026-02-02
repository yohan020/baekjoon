import sys

input = sys.stdin.readline
def solve():
    N = int(input())

    max_r, min_r = float('-inf'), float('inf')
    max_c, min_c = float('-inf'), float('inf')

    for _ in range(N):
        r, c = map(int, input().split())
        max_r = max(max_r, r)
        min_r = min(min_r, r)
        max_c = max(max_c, c)
        min_c = min(min_c, c)

    diff_c = max_c - min_c
    diff_r = max_r - min_r

    time_r = (diff_r + 1) // 2
    time_c = (diff_c + 1) // 2

    print(max(time_r, time_c))
    
if __name__ == "__main__":
    solve()