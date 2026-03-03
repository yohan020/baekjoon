import sys

input = sys.stdin.readline
def solve():
    N = int(input())
    ice = [tuple(map(int, input().split())) for _ in range(N)]

    ice.sort(key=lambda x: x[1], reverse=True)

    best_flavor, best_score = ice[0]

    same_flavor_max = 0
    diff_flavor_max = 0

    for i in range(1, N):
        flavor, score = ice[i]
        if flavor == best_flavor:
            if same_flavor_max == 0:
                same_flavor_max = score
        else:
            if diff_flavor_max == 0:
                diff_flavor_max = score
        if same_flavor_max > 0 and diff_flavor_max > 0:
            break
    ans = max(best_score, best_score + same_flavor_max // 2, best_score + diff_flavor_max )
    print(ans)

    

if __name__ == "__main__":
    solve()