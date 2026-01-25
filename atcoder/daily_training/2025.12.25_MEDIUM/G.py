import sys

input = sys.stdin.readline

def solve():
    H, W, K = map(int, input().split())
    grid = [input().strip() for _ in range(H)]
    ans = float('inf')

    def check(s):
        nonlocal ans
        n = len(s)
        if n < K: return
        
        cnt_x = 0
        cnt_dot = 0
        # 초기 윈도우 설정
        for i in range(K):
            if s[i] == 'x': cnt_x += 1
            elif s[i] == '.': cnt_dot += 1
        
        if cnt_x == 0:
            if cnt_dot < ans: ans = cnt_dot
            
        # 윈도우 슬라이딩
        for i in range(n - K):
            # 빠지는 문자 s[i]
            if s[i] == 'x': cnt_x -= 1
            elif s[i] == '.': cnt_dot -= 1
            
            # 들어오는 문자 s[i+K]
            if s[i+K] == 'x': cnt_x += 1
            elif s[i+K] == '.': cnt_dot += 1
            
            if cnt_x == 0:
                if cnt_dot < ans: ans = cnt_dot

    # 가로 방향 확인
    for i in range(H):
        check(grid[i])
        
    # 세로 방향 확인
    for j in range(W):
        # 열(column) 문자열 생성
        col = [grid[i][j] for i in range(H)]
        check(col)

    print(ans if ans != float('inf') else -1)

    


    

if __name__ == "__main__":
    solve()