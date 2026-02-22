import sys

input = sys.stdin.readline
def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    exist = set(A)
    ans = 0

    for i in range(K):
        if i in exist:
            ans += 1
        else:
            break
    print(ans)

            

if __name__ == "__main__":
    solve()