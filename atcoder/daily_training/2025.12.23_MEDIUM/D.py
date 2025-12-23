import sys

input = sys.stdin.readline

def solve():
    S = ['0'] + list(input())
    bowling = [[S[7]],[S[4]],[S[2], S[8]], [S[1], S[5]], [S[3], S[9]], [S[6]], [S[10]]]
    if S[1] == '1':
        print('No')
        return
    for i in range(6):
        for j in range(i+2, 7):
            if bowling[i].count('1') >= 1 and bowling[j].count('1') >= 1:
                for k in range(i+1, j):
                    if bowling[k].count('1') == 0:
                        print('Yes')
                        return
    print('No')

if __name__ == "__main__":
    solve()