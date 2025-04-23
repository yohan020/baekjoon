import sys
input = sys.stdin.readline

def split_rows_and_cols(matrix):
    rows = [row[:] for row in matrix]
    cols = [[row[j] for row in matrix] for j in range(len(matrix[0]))]
    return rows, cols

def solve(line):
    bridge = [False] * N
    global cnt
    now = 1
    while now < N:
        H = line[now-1] - line[now]
        if abs(H) >= 2:
            return
        if H == 1:
            if now - 1 + L >= N:
                return
            for i in range(1, L, 1):
                if line[now] != line[now+i] or bridge[now+i]:
                    return
            for i in range(0, L, 1):
                bridge[now+i] = True
            now += L
        elif H == -1:
            if now - L < 0 or bridge[now-1]:
                return
            for i in range(1, L, 1):
                if line[now-1] != line[now-1-i] or bridge[now-1-i]:
                    return
            for i in range(0, L, 1):
                bridge[now-1-i] = True
    
            now += 1
        else:
            now += 1
    if now == N:
        cnt += 1



N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

rows, cols = split_rows_and_cols(board)

cnt = 0
for i in range(N):
    solve(rows[i])
    solve(cols[i])
print(cnt)