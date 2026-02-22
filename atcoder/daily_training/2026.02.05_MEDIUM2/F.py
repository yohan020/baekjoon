import sys

input = sys.stdin.readline
def solve():
    N, M = map(int, input().split())
    B = list(map(int, input().split()))
    W = list(map(int, input().split()))

    B.sort(reverse=True)
    W.sort(reverse=True)
    
    current_sum = sum(b for b in B if b > 0)
    ans = current_sum

    limit = min(N, M)
    for i in range(limit):
        w_val = W[i]
        b_val = B[i]

        current_sum += w_val
        if b_val < 0:
            current_sum += b_val
        ans = max(ans, current_sum)

    print(ans)

if __name__ == "__main__":
    solve()