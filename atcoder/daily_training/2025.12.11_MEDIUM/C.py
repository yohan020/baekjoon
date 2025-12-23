import sys

input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    ans = 0
    left = K
    for a in A:
        if left < a:
            ans += 1
            left = K - a
        else:
            left -= a
    
    print(ans+1)

if __name__ == "__main__":
    solve()