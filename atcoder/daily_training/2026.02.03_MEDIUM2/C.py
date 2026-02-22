import sys

input = sys.stdin.readline
def solve():
    small_char = set("abcdefghijklmnopqrstuvwxyz")
    large_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    S = input().strip()

    small_cnt = 0
    large_cnt = 0
    for s in S:
        if s in small_char:
            small_cnt += 1
        elif s in large_char:
            large_cnt += 1
    if large_cnt > small_cnt:
        print(S.upper())
    else:
        print(S.lower())
    

if __name__ == "__main__":
    solve()