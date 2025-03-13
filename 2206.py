from collections import deque
import sys

input = sys.stdin.readline

def bfs():
    result = 987654321
    q = deque()
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = True
    q.append((0, 0, False, 1))
    while q:
        x, y, crash, cnt = q.popleft()
        if x == M - 1 and y == N - 1:
            return cnt
        
        for d in dir:
            temp_y = y + d[0]
            temp_x = x + d[1]
            
            if temp_x < 0 or M <= temp_x or temp_y < 0 or N <= temp_y: continue

            if board[temp_y][temp_x] == '1' and not crash and not visited[temp_y][temp_x][1]:
                q.append((temp_x, temp_y, True, cnt+1))
                visited[temp_y][temp_x][1] = True
            elif board[temp_y][temp_x] == '0' and not visited[temp_y][temp_x][crash]:
                visited[temp_y][temp_x][crash] = True
                q.append((temp_x, temp_y, crash, cnt+1))

    return -1


dir = [(-1,0),(1,0),(0,1),(0,-1)]

N, M = map(int, input().split())
board = list(str(input()) for _ in range(N))

print(bfs())