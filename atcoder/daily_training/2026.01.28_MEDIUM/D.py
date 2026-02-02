import sys

input = sys.stdin.readline

def check_diff_len(s, t):
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i + 1)
            return
    print(len(s) + 1)


def solve():
    S = input().strip()
    T = input().strip()
    if S == T:
        print(0)
        return
    elif len(S) <= len(T):
        check_diff_len(S, T)
    else:
        check_diff_len(T, S)
        

if __name__ == "__main__":
    solve()