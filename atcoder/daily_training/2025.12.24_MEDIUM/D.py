import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    score = list(map(int, input().split()))
    score.sort()
    for _ in range(N):
        score.pop(0)
        score.pop(-1)
    print(sum(score)/len(score))

if __name__ == "__main__":
    solve()