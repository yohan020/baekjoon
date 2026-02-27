import sys

input = sys.stdin.readline
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    res = [A[0]]
    for i in range(N-1):
        if abs(A[i] - A[i+1]) == 1:
            res.append(A[i+1])
        else:
            if A[i] < A[i+1]:
                for j in range(A[i]+1, A[i+1]+1):
                    res.append(j)
            elif A[i] > A[i+1]:
                for j in range(A[i]-1, A[i+1]-1, -1):
                    res.append(j)
            else:
                res.append(A[i]+1)
    print(*res)


if __name__ == "__main__":
    solve()