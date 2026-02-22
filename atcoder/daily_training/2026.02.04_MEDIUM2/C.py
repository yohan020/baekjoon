import sys

input = sys.stdin.readline
def solve():
    N, M = map(int, input().split())
    problems = []
    for _ in range(N):
        S = input().strip()
        problems.append(S)
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            cnt = 0
            for k in range(M):
                if problems[i][k] == 'o' or problems[j][k] == 'o':
                    cnt += 1
            if cnt == M:
                ans += 1
    print(ans)
    

if __name__ == "__main__":
    solve()