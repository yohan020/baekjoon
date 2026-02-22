import sys

input = sys.stdin.readline
def solve():
    N, K = map(int, input().split())
    score_board = []
    for i in range(N):
        score = sum(map(int, input().split()))
        score_board.append(score)
    sorted_score = sorted(score_board, reverse=True)
    standard_score = sorted_score[K-1]
    for i in range(N):
        if score_board[i] + 300 >= standard_score:
            print("Yes")
        else:
            print("No")
if __name__ == "__main__":
    solve()