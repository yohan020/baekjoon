import sys
import collections
input = sys.stdin.readline

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def main():
    n, m = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(n)]
    dist = [[-1] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 2:
                start = (i, j)
                dist[i][j] = 0
    queue = collections.deque([start])
    while queue:
        x, y = queue.popleft()
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] != 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = 0
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 0 and dist[i][j] == -1:
                dist[i][j] = 0
            elif maze[i][j] == 1 and dist[i][j] == -1:
                dist[i][j] = -1
    for row in dist:
        print(' '.join(map(str, row)))
if __name__ == "__main__":
    main()