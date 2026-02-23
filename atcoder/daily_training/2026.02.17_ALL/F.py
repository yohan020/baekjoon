import sys

input = sys.stdin.readline
def solve():
    h_1, h_2, h_3, w_1, w_2, w_3 = map(int, input().split())
    ans = 0
    a_11_max = min(h_1, w_1) - 1
    a_12_max = min(h_1, w_2) - 1
    a_21_max = min(h_2, w_1) - 1
    a_22_max = min(h_2, w_2) - 1
    for a_11 in range(1, a_11_max + 1):
        for a_12 in range(1, a_12_max + 1):
            for a_21 in range(1, a_21_max + 1):
                for a_22 in range(1, a_22_max + 1):
                    a_13 = h_1 - a_11 - a_12
                    a_23 = h_2 - a_21 - a_22
                    a_31 = w_1 - a_11 - a_21
                    a_32 = w_2 - a_12 - a_22
                    a_33 = h_3 - a_31 - a_32
                    if a_13 > 0 and a_23 > 0 and a_31 > 0 and a_32 > 0 and a_33 > 0:
                        if a_13 + a_23 + a_33 == w_3:
                            ans += 1
    print(ans)

if __name__ == "__main__":
    solve()