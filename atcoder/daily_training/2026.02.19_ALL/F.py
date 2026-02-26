import sys

input = sys.stdin.readline
def solve():
    N = int(input())
    K = list(map(int, input().split()))

    total_sum = sum(K)
    ans = float('inf')

    def dfs(index, current_A_sum):
        nonlocal ans
        if index == N:
            current_B_sum = total_sum - current_A_sum
            max_group = max(current_A_sum, current_B_sum)
            ans = min(ans, max_group)
            return
        
        dfs(index + 1, current_A_sum + K[index])
        dfs(index + 1, current_A_sum)
    dfs(0, 0)
    print(ans)

if __name__ == "__main__":
    solve()