import sys

input = sys.stdin.readline
def solve():
    N, T, P = map(int, input().split())
    L = list(map(int, input().split()))
    L.sort()

    start_idx = 0
    satisfied = 0
    for i in range(N-1, -1, -1):
        if L[i] >= T:
            start_idx = i
            satisfied += 1
        else:
            break
    remain = P - satisfied
    if remain <= 0:
        print(0)
    else:
        print(T - L[start_idx - remain])
if __name__ == "__main__":
    solve()