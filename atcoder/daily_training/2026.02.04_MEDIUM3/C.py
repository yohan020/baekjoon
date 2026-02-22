import sys

input = sys.stdin.readline
def solve():
    N, M = map(int, input().split())
    son = [0] * (N + 1)
    for _ in range(M):
        a, b = map(str, input().split())
        if b == 'M':
            son[int(a)] += 1
        if son[int(a)] == 1 and b == 'M':
            print('Yes')
        else:
            print('No')



if __name__ == "__main__":
    solve()