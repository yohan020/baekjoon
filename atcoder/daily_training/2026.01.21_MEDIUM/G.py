import sys

input = sys.stdin.readline
def solve():
    T = int(input())
    for _ in range(T):
        N, M, K = map(int, input().split())

        S = input().strip()

        adj = [[] for _ in range(N + 1)]
        for _ in range(M):
            u, v = map(int, input().split())
            adj[u].append(v)

        dp = [False] * (N + 1)
        for i in range(1, N + 1):
            if S[i - 1] == 'A':
                dp[i] = True
            else:
                dp[i] = False
        
        total_moves = 2 * K
        for i in range(1, total_moves+1):
            next_dp = [False] * (N + 1)

            is_alice_turn = (i % 2 == 0)

            for u in range(1, N + 1):
                if is_alice_turn:
                    can_win = False
                    for v in adj[u]:
                        if dp[v]:
                            can_win = True
                            break
                    next_dp[u] = can_win
                else:
                    all_win = True
                    for v in adj[u]:
                        if not dp[v]:
                            all_win = False
                            break
                    next_dp[u] = all_win
            dp = next_dp
        
        if dp[1]:
            print("Alice")
        else:
            print("Bob")


if __name__ == "__main__":
    solve()