import sys

input = sys.stdin.readline
def solve():
    X = input().rstrip()
    idx = len(X) - 1
    while idx >= 0 and X[idx] == '0':
        idx -= 1
    if idx < 0:
        print(0)
    elif X[idx] == '.':
        print(X[:idx])
    else:
        print(X[:idx+1])

if __name__ == "__main__":
    solve()