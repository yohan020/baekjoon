import sys
from collections import Counter

input = sys.stdin.readline
def solve():
    S = input().rstrip()
    arr = [0] * 101
    counter = Counter(S)
    for c in counter:
        arr[counter[c]] += 1
    for i in range(1, 101):
        if arr[i] == 0 or arr[i] == 2:
            continue
        print("No")
        return
    print("Yes")
if __name__ == "__main__":
    solve()