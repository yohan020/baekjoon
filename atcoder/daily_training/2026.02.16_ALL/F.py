import sys

input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    C = []
    for _ in range(M):
        _ = int(input())
        c = set(map(int, input().split()))
        C.append(c)
    
    ans = 0
    def dfs(idx, current_set):
        nonlocal ans

        if idx == M:
            if len(current_set) == N:
                ans += 1
            return
        dfs(idx + 1, current_set)
        dfs(idx + 1, current_set | C[idx])
    
    dfs(0, set())
    print(ans)

if __name__ == "__main__":
    solve()