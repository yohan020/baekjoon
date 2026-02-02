import sys
from collections import defaultdict

input = sys.stdin.readline
def solve():
    N, K = map(int, input().split())
    S = input().strip()

    MOD = 998244353

    dp = defaultdict(int)
    dp[""] = 1

    for i in range(N):
        next_dp = defaultdict(int)

        possible_chars = []
        if S[i] == 'A': possible_chars = ['A']
        elif S[i] == 'B': possible_chars = ['B']
        else: possible_chars = ['A', 'B']

        for curr_str, count in dp.items():
            for char in possible_chars:
                new_str = curr_str + char
                if len(new_str) == K:
                    if new_str == new_str[::-1]:
                        continue
                    next_state = new_str[1:]
                else:
                    next_state = new_str
                next_dp[next_state] = (next_dp[next_state] + count) % MOD
        dp = next_dp
    result = sum(dp.values()) % MOD
    print(result)

if __name__ == "__main__":
    solve()