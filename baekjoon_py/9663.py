
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
visited_saseon1 = [False] * (2 * N - 1)
visited_saseon2 = [False] * (2 * N - 1)
dfs(0)
print(result)
