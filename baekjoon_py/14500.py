import sys

input = sys.stdin.readline

dir = [[-1,0], [1,0], [0,-1],[0,1]]

def DFS(start_x, start_y):
    stack = [(start_x, start_y, 1, board[start_y][start_x], [(start_x, start_y)])]
    global result
    max_score = max(max(N) for N in board)
    while stack:
        x, y, cnt, score, visited = stack.pop()
        if score + (4 - cnt) * max_score <= result: #가지치기, 만약 값이 너무 작다면 가망이 없으므로 그냥 패스해서 속도 올림
            continue
        if cnt == 4:
            result = max(result, score)
            continue
        for i in range(4):
            temp_x = x + dir[i][1]
            temp_y = y + dir[i][0]
            if 0 <= temp_y < N and 0 <= temp_x < M:
                if (temp_x, temp_y) in visited:
                    continue
                new_visited = visited + [(temp_x, temp_y)]
                stack.append((temp_x, temp_y, cnt + 1, score + board[temp_y][temp_x], new_visited))


def T(x, y):
    global result
    if x < M - 1 and y < N - 2:
        result = max(result, board[y][x]+board[y+1][x]+board[y+1][x+1]+board[y+2][x])
        result = max(result, board[y][x+1]+board[y+1][x+1]+board[y+1][x]+board[y+2][x+1])
    if x < M - 2 and y < N - 1:
        result = max(result, board[y][x]+board[y][x+1]+board[y][x+2]+board[y+1][x+1])
        result = max(result, board[y][x+1]+board[y+1][x]+board[y+1][x+1]+board[y+1][x+2])

result = 0
N, M = map(int, input().split())
board = []

visited = set()
for _ in range(N):
    board.append(list(map(int, input().split())))
for i in range(N):
    for j in range(M):
        DFS(j, i)
        T(j, i)
print(result)