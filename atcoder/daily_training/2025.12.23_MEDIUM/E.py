import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    poem = []
    poem_set = set()
    max_value = 0
    max_idx = 0
    for i in range(N):
        S, T = input().split()
        if S in poem_set:
            continue
        poem_set.add(S)
        poem.append((S, T))
        if int(T) > max_value:
            max_value = int(T)
            max_idx = i
    print(max_idx + 1)
if __name__ == "__main__":
    solve()