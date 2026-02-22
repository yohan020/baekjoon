import sys

input = sys.stdin.readline
def solve():
    H, W = map(int, input().split())
    S = [input().rstrip() for _ in range(H)]
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                cnt = 0
                for d in dir:
                    ni, nj = i + d[0], j + d[1]
                    if ni < 0 or ni >= H or nj < 0 or nj >= W:
                        continue
                    if S[ni][nj] == '#':
                        cnt += 1
                if cnt == 0 or cnt == 1 or cnt == 3:
                    print("No")
                    return
    print("Yes")
                
                

if __name__ == "__main__":
    solve()