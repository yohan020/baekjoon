import sys

input = sys.stdin.readline

def solve():
    H, W = map(int, input().split())
    A = [input().strip() for _ in range(H)]
    x_1, y_1, x_2, y_2 = -1, -1, -1, -1
    for i in range(H):
        for j in range(W):
            if A[i][j] == 'o':
                if x_1 == -1:
                    x_1, y_1 = i, j
                else:
                    x_2, y_2 = i, j
    print(abs(x_1-x_2)+abs(y_1-y_2))


if __name__ == "__main__":
    solve()