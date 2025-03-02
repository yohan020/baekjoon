def dfs(row):
    global result
    if row == N:
        result += 1
        return
    
    for col in range(N):
        if visited_col[col] or visited_saseon1[row - col + (N - 1)] or visited_saseon2[row + col]:  
            continue
        visited_col[col] = True
        visited_saseon1[row - col + (N - 1)] = True
        visited_saseon2[row + col] = True
        dfs(row + 1)
        visited_col[col] = False
        visited_saseon1[row - col + (N - 1)] = False
        visited_saseon2[row + col] = False

N = int(input())
result = 0

visited_col = [False] * N
visited_saseon1 = [False] * (2 * N - 1) # 왼쪽에서 오른쪽 대각선, (3,2) (2,1) / (4,2) (3,1) 행과 열의 차이가 다 같음
visited_saseon2 = [False] * (2 * N - 1) # 오른쪽에서 왼쪽 대각선, (3,2) (4,1) / (4,2) (3,3) 헹과 열의 합이 다 같음
dfs(0)
print(result)
