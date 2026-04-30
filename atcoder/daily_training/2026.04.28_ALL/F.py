import sys
from itertools import permutations

input = sys.stdin.readline

def solve():
    C = []
    for _ in range(3):
        C += list(map(int, input().split()))

    lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    good = 0
    total = 0

    for order in permutations(range(9)):
        total += 1

        seen_times = [0] * 9
        for t, cell in enumerate(order):
            seen_times[cell] = t
        
        disappointed = False

        for line in lines:
            a, b, c = line

            if C[a] == C[b] and C[a] != C[c]:
                if seen_times[c] > seen_times[a] and seen_times[c] > seen_times[b]:
                    disappointed = True

            if C[a] == C[c] and C[a] != C[b]:
                if seen_times[b] > seen_times[a] and seen_times[b] > seen_times[c]:
                    disappointed = True

            if C[b] == C[c] and C[b] != C[a]:
                if seen_times[a] > seen_times[b] and seen_times[a] > seen_times[c]:
                    disappointed = True

        if not disappointed:
            good += 1

    print(good / total)

if __name__ == "__main__":
    solve()
