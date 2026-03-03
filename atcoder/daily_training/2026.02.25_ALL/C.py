import sys

input = sys.stdin.readline
def solve():
    board = [input().rstrip() for _ in range(8)]
    abc = 'abcdefgh'
    for i in range(8):
        for j in range(8):
            if board[i][j] == '*':
                print(abc[j] + str(8 - i))
                return

if __name__ == "__main__":
    solve()