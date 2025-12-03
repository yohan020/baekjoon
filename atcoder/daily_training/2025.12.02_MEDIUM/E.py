import sys

input = sys.stdin.readline
MOD = 998244353

def solve():
    try:
        line = input().strip()
        if not line:
            return
        N = int(line)
    except ValueError:
        return

    dp = [0] * 10
    for j in range(1, 10):
        dp[j] = 1

    for _ in range(N-1):
        new_dp = [0] * 10
        for j in range(1, 10):
            count = dp[j]
            if j > 1:
                count += dp[j-1]
            if j < 9:
                count += dp[j+1]
            new_dp[j] = count % MOD
        dp = new_dp
    
    print(sum(dp) % MOD)
            

if __name__ == "__main__":
    solve()