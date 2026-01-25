import sys

input = sys.stdin.readline

def solve():
    D, F = map(int, input().split())
    day = F
    while day <= D:
        day += 7
    print(day-D)
    
if __name__ == "__main__":
    solve()