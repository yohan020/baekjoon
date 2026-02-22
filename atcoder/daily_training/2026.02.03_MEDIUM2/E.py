import sys

input = sys.stdin.readline
def solve():
    N = int(input())
    P = list(map(int, input().split()))

    i = N - 1
    while i > 0 and P[i - 1] < P[i]:
        i -= 1
    
    j = N - 1
    while P[j] > P[i - 1]:
        j -= 1
    
    P[i - 1], P[j] = P[j], P[i - 1]
    P[i:] = reversed(P[i:])
    print(*P)
    

if __name__ == "__main__":
    solve()