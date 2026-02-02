import sys

input = sys.stdin.readline
def solve():
    x1, y1, x2, y2 = map(int, input().split())
    dots = [(x1+1, y1+2), (x1+2, y1+1), (x1+1, y1-2), (x1+2, y1-1), (x1-1, y1+2), (x1-2, y1+1), (x1-1, y1-2), (x1-2, y1-1)]
    for x, y in dots:
        distance = ((x - x2) ** 2 + (y - y2) ** 2)
        if distance == 5:
            print("Yes")
            return
    print("No")
    

if __name__ == "__main__":
    solve()