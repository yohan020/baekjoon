import sys

input = sys.stdin.readline

def first_action(s, t):
    wrong = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            wrong += 1
        if wrong >= 2:
            return False
    return True

def second_action(s, t):
    wrong_idx = -1
    for i in range(len(t)):
        if s[i] != t[i]:
            wrong_idx = i
            break
    if wrong_idx == -1:
        return True

    s = s[:wrong_idx] + s[wrong_idx+1:]
    return s == t

def third_action(s, t):
    wrong_idx = -1
    for i in range(len(s)):
        if s[i] != t[i]:
            wrong_idx = i
            break
    if wrong_idx == -1:
        return True

    s = s[:wrong_idx] + t[wrong_idx] + s[wrong_idx:]
    return s == t

def solve():
    N, T = map(str, input().split())
    S = []
    for _ in range(int(N)):
        S.append(input().strip())
    res = []
    for i in range(int(N)):
        len_diff = len(S[i]) - len(T)
        if len_diff == 0:
            if S[i] == T:
                res.append(i+1)
            elif first_action(S[i], T):
                res.append(i+1)
        elif len_diff == 1:
            if second_action(S[i], T):
                res.append(i+1)
        elif len_diff == -1:
            if third_action(S[i], T):
                res.append(i+1)
    print(len(res))
    print(' '.join(map(str, res)))

            

if __name__ == "__main__":
    solve()