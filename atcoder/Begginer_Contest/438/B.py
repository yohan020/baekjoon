import sys

input = sys.stdin.readline

def cal(s, t):
    if s < t:
        s += 10
    return abs(s-t)

def solve():
    N, M = map(int, input().split())
    S = list(str(input().strip()))
    T = list(str(input().strip()))
    
    min_cnt = float("inf")

    for i in range(N-M+1):
        cnt = 0
        for j in range(M):
            cnt += cal(int(S[i+j]), int(T[j]))
        min_cnt = min(min_cnt, cnt)
    print(min_cnt)
    
if __name__ == "__main__":
    solve()