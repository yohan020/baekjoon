import sys
from itertools import permutations

input = sys.stdin.readline
def solve():
    M = int(input())
    S = []

    for _ in range(3):
        S.append(list(input().rstrip()))
    
    ans = float('inf')

    for target in range(10):
        target_str = str(target)

        if all(target_str in s for s in S):
            for p in permutations([0, 1, 2]):
                time = 0

                while S[p[0]][time % M] != target_str:
                    time += 1
                time += 1
                while S[p[1]][time % M] != target_str:
                    time += 1
                time += 1
                while S[p[2]][time % M] != target_str:
                    time += 1
                
                ans = min(ans, time)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    solve()