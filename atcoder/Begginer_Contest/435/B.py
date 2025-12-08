import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    ans = sum([i for i in range(1, N+1)])
    for i in range(N):
        for j in range(i, N):
            n = A[i:j+1]
            s = sum(n)
            for k in n:
                if s % k == 0:
                    ans -= 1
                    break
    print(ans)
            
if __name__ == "__main__":
    solve()