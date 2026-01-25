import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))
    C = [0] + list(map(int, input().split()))
    DP = [[-float("inf")]*3 for _ in range(N+1)]
    DP[1][0] = A[1]
    for i in range(2, N+1):
        DP[i][0] = DP[i-1][0] + A[i]
        DP[i][1] = max(DP[i-1][0], DP[i-1][1]) + B[i]
        DP[i][2] = max(DP[i-1][1], DP[i-1][2]) + C[i]
    print(DP[N][2])

    
if __name__ == "__main__":
    solve()