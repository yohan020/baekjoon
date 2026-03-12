import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    
    count = [0] * (N + 1)

    limit = int(N ** 0.5) + 1

    sq = [i ** 2 for i in range(limit)]

    for i in range(1, limit):
        for j in range(i + 1, limit):
            val = sq[i] + sq[j]
            if val > N:
                break
            count[val] += 1
    res = [i for i in range(1, N + 1) if count[i] == 1]
    print(len(res))
    print(*res)

if __name__ == "__main__":
    solve()