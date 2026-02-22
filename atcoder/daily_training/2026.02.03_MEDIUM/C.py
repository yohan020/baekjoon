import sys

input = sys.stdin.readline
def solve():
    N, M = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    C = list(A) + list(B)
    C.sort()

    flag = 0
    for c in C:
        if c in A:
            if flag == 1:
                print("Yes")
                return
            flag = 1
        else:
            flag = 0
    print("No")

if __name__ == "__main__":
    solve()