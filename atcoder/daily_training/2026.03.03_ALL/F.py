import sys

input = sys.stdin.readline
def solve():
    X, A, D, N = map(int, input().split())
    min_n = min(A, A + D * (N - 1))
    max_n = max(A, A + D * (N - 1))
    if X < min_n:
        print(abs(X - min_n))
    elif X > max_n:
        print(abs(X - max_n))
    else:
        if D == 0:
            print(abs(X - A))
        else:
            d = abs(D)
            mod = abs((X - A) % d)
            print(min(mod, d - mod))

if __name__ == "__main__":
    solve()