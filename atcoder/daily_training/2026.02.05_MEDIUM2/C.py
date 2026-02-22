import sys

input = sys.stdin.readline
def solve():
    p, q = map(str, input().split())
    distance = [0, 3, 4, 8, 9, 14, 23]
    dots = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
    print(abs(distance[dots[q]] - distance[dots[p]]))

if __name__ == "__main__":
    solve()