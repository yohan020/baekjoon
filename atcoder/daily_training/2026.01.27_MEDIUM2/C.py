import sys

input = sys.stdin.readline
def solve():
    A, M, L, R = map(int, input().split())
    left_cnt = (L - A) // (-M)
    left_t = A - M * left_cnt
    right_cnt = (R - left_t) // M
    right_t = left_t + M * right_cnt
    ans = (right_t - left_t) // M + 1
    print(ans)
if __name__ == "__main__":
    solve()