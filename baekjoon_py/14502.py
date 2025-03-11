import sys
from itertools import combinations
from collections import deque

dir = [[-1, 0],[1, 0],[0, -1],[0, 1]]

def BFS():
    virus_cnt = 0
    q = deque()
    lab_copy = [row[:] for row in lab]
    for i in range(len(virus)):
        q.append(virus[i])
        virus_cnt += 1
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            temp_x = x + dx
            temp_y = y + dy
            if 0 <= temp_x < M and 0 <= temp_y < N:
                if lab_copy[temp_y][temp_x] == 0:
                    lab_copy[temp_y][temp_x] = 2
                    virus_cnt += 1
                    q.append((temp_x, temp_y))
    return virus_cnt



input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
virus = []
empty = []
wall_count = 0

for i in range(N*M):
    x = i % M
    y = i // M
    if lab[y][x] == 0:
        empty.append((x, y))
    elif lab[i // M][i % M] == 2:
        virus.append((i % M, i // M))
    elif lab[i // M][i % M] == 1:
        wall_count += 1

min_virus = N * M

for walls in combinations(empty, 3):
    for x, y in walls:
        lab[y][x] = 1
    virus_cnt = BFS()
    min_virus = min(min_virus, virus_cnt)
    for x, y in walls:
        lab[y][x] = 0

print(N*M - min_virus - wall_count - 3)