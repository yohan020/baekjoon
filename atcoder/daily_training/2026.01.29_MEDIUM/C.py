import sys

input = sys.stdin.readline
def solve():
    N = int(input())
    dots = []
    for _ in range(N):
        x, y = map(int, input().split())
        dots.append((x, y))
    for i in range(N):
        x1, y1 = dots[i]
        max_len = 0
        max_idx = -1
        for j in range(N):
            if i == j:
                continue
            x2, y2 = dots[j]
            l = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            if l > max_len:
                max_len = l
                max_idx = j
        print(max_idx + 1)


if __name__ == "__main__":
    solve()