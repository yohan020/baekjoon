import sys

input = sys.stdin.readline
def solve():
    A, B = map(str, input().split())
    A = A[::-1]
    B = B[::-1]
    l = min(len(A), len(B))
    for i in range(l):
        if int(A[i]) + int(B[i]) >= 10:
            print("Hard")
            return
    print("Easy")

if __name__ == "__main__":
    solve()