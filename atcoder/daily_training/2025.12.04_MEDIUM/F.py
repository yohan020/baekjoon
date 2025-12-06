import sys
input = sys.stdin.readline

def solve():
    A = [list(map(int, input().split())) for _ in range(9)]

    for a in A:
        s = set(a)
        if len(s) != 9:
            print("No")
            return
    for i in range(9):
        s = set(A[j][i] for j in range(9))
        if len(s) != 9:
            print("No")
            return
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            s = set(A[c][r] for c in range(i, i+3) for r in range(j, j+3))
            if len(s) != 9:
                print("No")
                return
    print("Yes")


if __name__ == "__main__":
    solve()