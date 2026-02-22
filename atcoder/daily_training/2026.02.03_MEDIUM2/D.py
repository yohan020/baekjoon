import sys

input = sys.stdin.readline
def solve():
    N, M = map(int, input().split())
    S_list = []
    for _ in range(N):
        S = input().strip()
        S_list.append(S[3:])
    count = 0
    T_set = set()
    for _ in range(M):
        T = input().strip()
        T_set.add(T)
    for S in S_list:
        if S in T_set:
            count += 1
    print(count)

if __name__ == "__main__":
    solve()