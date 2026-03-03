import sys

input = sys.stdin.readline
def solve():
    N, Q = map(int, input().split())
    S = list(input().rstrip())

    count = 0
    for i in range(N - 2):
        if S[i] == 'A' and S[i + 1] == 'B' and S[i + 2] == 'C':
            count += 1
    for _ in range(Q):
        x, c = input().split()
        x = int(x) - 1

        for i in range(x - 2, x + 1):
            if 0 <= i and i + 2 < N:
                if S[i] == 'A' and S[i + 1] == 'B' and S[i + 2] == 'C':
                    count -= 1
        
        S[x] = c

        for i in range(x - 2, x + 1):
            if 0 <= i and i + 2 < N:
                if S[i] == 'A' and S[i + 1] == 'B' and S[i + 2] == 'C':
                    count += 1
        
        print(count)




if __name__ == "__main__":
    solve()