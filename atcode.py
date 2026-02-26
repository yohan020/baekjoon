import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    dot = set()
    ans = 0
    for _ in range(N):
        x, y = map(int, input().split())
        dot.add((x, y))
    for i in dot:
        for j in dot:
            if i == j:
                continue
            if i[0] == j[0] or i[1] == j[1]:
                continue
            if (i[0], j[1]) in dot and (j[0], i[1]) in dot:
                ans += 1
    print(ans//4)
if __name__ == "__main__":
    solve()