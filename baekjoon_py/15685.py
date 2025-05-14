import sys
input = sys.stdin.readline

def dragon_curve(x, y, d, g):
    dir = [(1,0),(0,-1),(-1,0),(0,1)]
    seq = [d]
    for _ in range(g):
        seq += [(direction + 1) % 4 for direction in reversed(seq)]
    board[y][x] = True
    for direction in seq:
        x += dir[direction][0]
        y += dir[direction][1]
        board[y][x] = True
             

N = int(input())
board = [[False for _ in range(100)] for _ in range(100)]
for i in range(N):
    x, y, d, g = map(int, input().split())
    dragon_curve(x, y, d, g)
cnt = 0
for i in range(99):
    for j in range(99):
        if board[i][j] and board[i][j+1] and board[i+1][j] and board[i+1][j+1]:
            cnt += 1
print(cnt)
