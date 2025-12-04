import sys
from collections import deque 

input = sys.stdin.readline

def solve():
    # Read H, W
    try:
        line1 = input().split()
        if not line1: return # End of input
        H, W = map(int, line1)
    except ValueError: return

    board = [list(input().strip()) for _ in range(H)]
    
    start_pos = None
    
    for i in range(H):
        for j in range(W):
            if board[i][j] == 'S':
                start_pos = (i, j)
                break
        if start_pos:
            break
            
    # dist[x][y][switch_state]
    # switch_state: 0 = original, 1 = flipped
    # Initialize with -1
    dist = [[[-1] * 2 for _ in range(W)] for _ in range(H)]
    
    sx, sy = start_pos
    dist[sx][sy][0] = 0
    
    queue = deque()
    queue.append((sx, sy, 0))
    
    while queue:
        x, y, s = queue.popleft()
        d = dist[x][y][s]
        
        if board[x][y] == 'G':
            print(d)
            return

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < H and 0 <= ny < W:
                if board[nx][ny] == '#':
                    continue
                
                ns = s
                is_passable = False
                
                cell = board[nx][ny]
                
                if cell == 'S' or cell == 'G' or cell == '.':
                    is_passable = True
                elif cell == 'o':
                    if s == 0: is_passable = True
                    else: is_passable = False # Becomes 'x'
                elif cell == 'x':
                    if s == 0: is_passable = False
                    else: is_passable = True # Becomes 'o'
                elif cell == '?':
                    is_passable = True
                    ns = 1 - s # Toggle state
                
                if is_passable:
                    if dist[nx][ny][ns] == -1:
                        dist[nx][ny][ns] = d + 1
                        queue.append((nx, ny, ns))
                        
    print(-1)

if __name__ == "__main__":
    solve()