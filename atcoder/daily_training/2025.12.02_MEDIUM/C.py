import sys

input = sys.stdin.readline

def solve():
    s = input().strip()
    t = input().strip()
    dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
    if abs(dic[s[0]] - dic[s[1]]) > 1:
        s_len = 2
    else:
        s_len = 1
    if abs(dic[t[0]] - dic[t[1]]) > 1:
        t_len = 2
    else:
        t_len = 1
    if s == 'AE' or s == 'EA':
        s_len = 1
    if t == 'AE' or t == 'EA':
        t_len = 1
    if s_len == t_len:
        print("Yes")
    else:
        print("No")
    
if __name__ == "__main__":
    solve()