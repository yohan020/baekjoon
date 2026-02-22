import sys

def check(S):
    temp = set()
    for i in range(len(S)):
        temp.add(S[i])
        if len(temp) >= 2:
            return False
    return True

    

input = sys.stdin.readline
def solve():
    N = int(input())
    D = list(map(int, input().split()))

    ans = 0
    for i in range(1, N+1):
        for j in range(1, D[i-1] + 1):
            S = str(i) + str(j)
            if check(S):
                ans += 1
            
    print(ans)    

if __name__ == "__main__":
    solve()