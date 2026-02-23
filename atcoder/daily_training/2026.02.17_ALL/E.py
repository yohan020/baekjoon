import sys

input = sys.stdin.readline
def solve():
    Sx, Sy = map(int, input().split())
    Tx, Ty = map(int, input().split())

    if (Sx + Sy) % 2 == 0:
        SL, SR = Sx, Sx + 1
    else:
        SL, SR = Sx - 1, Sx
    
    if (Tx + Ty) % 2 == 0:
        TL, TR = Tx, Tx + 1
    else:
        TL, TR = Tx - 1, Tx

    dy = abs(Sy - Ty)

    M_left = SL - dy
    M_right = SR + dy

    extra_cost = 0
    if TL > M_right:
        extra_cost = (TL - M_right + 1) // 2
    elif TR < M_left:
        extra_cost = (M_left - TR + 1) // 2
    
    ans = dy + extra_cost
    print(ans)

if __name__ == "__main__":
    solve()