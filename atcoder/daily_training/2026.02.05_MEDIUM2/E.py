import sys
from collections import Counter

input = sys.stdin.readline
def solve():
    N = int(input())
    A = list(map(int, input().split()))

    counts = Counter(A)

    ans = 0

    for num, cnt in counts.items():
        if cnt >= 2:
            pair_count = (cnt * (cnt - 1)) // 2
            other_count = N - cnt
            ans += pair_count * other_count
    print(ans)
if __name__ == "__main__":
    solve()