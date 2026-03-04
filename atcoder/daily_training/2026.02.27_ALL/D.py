import sys

input = sys.stdin.readline

def first_weired_time(H, M):
    if H[0] == "2":
        if int(M[0]) <= 3:
            if second_weired_time(H, M):
                return True
        return False
    else:
        if second_weired_time(H, M):
            return True
        else:
            return False
    
def second_weired_time(H, M):
    if int(H[1]) <= 5:
        return True
    else:
        return False

def solve():
    H, M = map(str, input().split())
    if len(H) == 1:
        H = "0" + H
    if len(M) == 1:
        M = "0" + M

    while not first_weired_time(H, M):
        M = str((int(M) + 1) % 60)
        if M == "0":
            H = str((int(H) + 1) % 24)
        if len(H) == 1:
            H = "0" + H
        if len(M) == 1:
            M = "0" + M
    print(int(H), int(M))
if __name__ == "__main__":
    solve()