import sys

input = sys.stdin.readline
def solve():
    N = int(input())
    A = [1]
    for i in range(1, N + 1):
        S = 0
        for j in range(i):
            if len(str(A[j])) >= 2:
                for k in str(A[j]):
                    S += int(k)
            else:
                S += A[j]
        A.append(S)
    print(A[N])


if __name__ == "__main__":
    solve()