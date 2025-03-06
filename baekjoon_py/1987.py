import sys

input = sys.stdin.readline
print = sys.stdout.write

dir = [[-1,0], [1,0], [0,-1],[0,1]]

def DFS():
    stack = [(0, 0, 1, {board[0][0]})] 
    global result
    result = 0

    while stack:
        x, y, cnt, visited = stack.pop()
        result = max(result, cnt)
        for i in range(4):
            temp_x = x + dir[i][1]
            temp_y = y + dir[i][0]
            if 0 <= temp_x < C and 0 <= temp_y < R:
                if board[temp_y][temp_x] not in visited:
                    new_visited = visited.copy()
                    new_visited.add(board[temp_y][temp_x])
                    stack.append((temp_x, temp_y, cnt + 1, new_visited))


R, C = map(int, input().split())
board = []
stack = []
visited = set()
for _ in range(R):
    board.append(input())
visited.add(board[0][0])
result = 1
DFS()
print(str(result))