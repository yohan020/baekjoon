import sys

input = sys.stdin.readline
def solve():
    A, B = map(int, input().split())
    ans = 0
    
    if A < B:
        A, B = B, A
    
    while B > 0:
        if A % B == 0:
            ans += A // B - 1
            break
        ans += A // B
        A, B = B, A % B
    print(ans)

if __name__ == "__main__":
    solve()