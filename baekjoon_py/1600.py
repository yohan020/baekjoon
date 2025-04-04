from collections import deque
import sys

input = sys.stdin.readline

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
h_dir = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
visited = [[[float('inf') for _ in range(K+1)] for _ in range(W)] for _ in range(H)]

q = deque()
q.append((0,0,K,0))
visited[0][0][K] = 0
while q:
    x, y, horse, cnt = q.popleft()
    if (x, y) == (W-1, H-1):
        break
    for i_y, i_x in dir:
        temp_y = i_y + y
        temp_x = i_x + x
        if temp_y < 0 or H <= temp_y or temp_x < 0 or W <= temp_x: continue
        if board[temp_y][temp_x] == 1: continue
        if visited[temp_y][temp_x][horse] != float('inf'): continue
        visited[temp_y][temp_x][horse] = cnt+1
        q.append((temp_x, temp_y, horse, cnt+1))
    if horse <= 0: continue
    for i_y, i_x in h_dir:
        temp_y = i_y + y
        temp_x = i_x + x
        if temp_y < 0 or H <= temp_y or temp_x < 0 or W <= temp_x: continue
        if board[temp_y][temp_x] == 1: continue
        if visited[temp_y][temp_x][horse-1] != float('inf'): continue
        visited[temp_y][temp_x][horse-1] = cnt+1
        q.append((temp_x, temp_y, horse-1, cnt+1))
result = min(visited[H-1][W-1])
if result == float('inf'):
    print(-1)
else:
    print(result)
