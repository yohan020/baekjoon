import sys
from collections import Counter

input = sys.stdin.readline
def solve():
    S = input().strip()
    counter = Counter(S)

    for char in S:
        if counter[char] == 1:
            print(char)
            return
if __name__ == "__main__":
    solve()