import sys
from collections import Counter

input = sys.stdin.readline
def solve():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    count = Counter(A)
    ans = 0
    for a in count:
        b = S - a

        if b not in count:
            continue
        if a > b:
            continue
        if a == b:
            ans += count[a] * (count[a] - 1) // 2
        else:
            ans += count[a] * count[b]
    print(ans)

if __name__ == "__main__":
    solve()