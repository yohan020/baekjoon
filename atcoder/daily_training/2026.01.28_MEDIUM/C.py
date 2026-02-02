import sys

input = sys.stdin.readline
def solve():
    K, G, M = map(int, input().split())
    water_g = 0
    water_m = 0
    for _ in range(K):
        if water_g == G:
            water_g = 0
            continue
        elif water_m == 0:
            water_m = M
            continue
        else:
            if water_m + water_g > G:
                water_m -= (G - water_g)
                water_g = G
            else:
                water_g += water_m
                water_m = 0
    print(f'{water_g} {water_m}')

if __name__ == "__main__":
    solve()