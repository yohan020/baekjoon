import sys

input = sys.stdin.readline

def rotate(S):
    return list(zip(*S[::-1]))

def find_left_top(S):
    for i in range(len(S)):
        for j in range(len(S)):
            if S[i][j] == '#':
                return (i, j)

def is_same(S, T):
    N = len(S)
    Si, Sj = find_left_top(S)
    Ti, Tj = find_left_top(T)
    offset_i = Ti - Si
    offset_j = Tj - Sj
    for i in range(N):
        for j in range(N):
            ii = i+offset_i
            jj = j+offset_j
            if 0 <= ii < N and 0 <= jj < N:
                if S[i][j] != T[ii][jj]:
                    return False
            else:
                if S[i][j] == '#':
                    return False
    return True

def solve():
    N = int(input())
    S = [str(input().strip()) for _ in range(N)]
    T = [str(input().strip()) for _ in range(N)]
    
    cntS = sum(1 for i in range(N) for j in range(N) if S[i][j] == '#')
    cntT = sum(1 for i in range(N) for j in range(N) if T[i][j] == '#')
    if cntS != cntT:
        print("No")
        return
    
    for _ in range(4):
        if is_same(S, T):
            print("Yes")
            return
        S = rotate(S)
    print("No")
    

if __name__ == "__main__":
    solve()