import sys

input = sys.stdin.readline
def solve():
    dots = []
    for _ in range(3):
        x, y = map(int, input().split())
        dots.append((x, y))
    lengths = []
    for i in range(3):
        x1, y1 = dots[i]
        x2, y2 = dots[(i + 1) % 3]
        length = ((x1 - x2) ** 2 + (y1 - y2) ** 2)
        lengths.append(length)
    lengths.sort()
    if lengths[0] + lengths[1] == lengths[2]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()