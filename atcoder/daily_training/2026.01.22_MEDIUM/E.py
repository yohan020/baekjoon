import sys

input = sys.stdin.readline
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = {}
    for i in A:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    n = []
    for k in cnt.items():
        if k[1] == 1:
            n.append(k[0])
    if len(n) == 0:
        print(-1)
    else:
        print(A.index(max(n))+1)





if __name__ == "__main__":
    solve()