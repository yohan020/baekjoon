import sys

input = sys.stdin.readline
def solve():
    N, Q = map(int, input().split())
    
    S = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        row_str = input().strip()
        for j in range(1, N + 1):
            val = 1 if row_str[j - 1] == 'B' else 0
            S[i][j] = S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1] + val
        
    total_black_cnt = S[N][N]

    def calc(h, w):
        q_h, r_h = divmod(h, N)
        q_w, r_w = divmod(w, N)

        res = q_h * q_w * total_black_cnt

        res += S[r_h][N] * q_w
        res += S[N][r_w] * q_h
        res += S[r_h][r_w]

        return res
        
    for _ in range(Q):
        A, B, C, D = map(int, input().split())
        ans = calc(C + 1, D + 1) - calc(A, D + 1) - calc(C + 1, B) + calc(A, B)
        print(ans)
if __name__ == "__main__":
    solve()