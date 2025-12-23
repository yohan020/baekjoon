import sys

input = sys.stdin.readline

def solve():
    N, A, B = map(int, input().split())
    D = list(map(int, input().split()))
    
    W = A + B

    remainders = set()
    for d in D:
        remainders.add(d % W)
    
    S = sorted(list(remainders))
    K = len(S)
    
    extended_S = S + [x + W for x in S]

    for i in range(len(S)):
        span = extended_S[i+K-1] - extended_S[i]

        if span < A:
            print("Yes")
            return
    
    print("No")

        

if __name__ == "__main__":
    solve()