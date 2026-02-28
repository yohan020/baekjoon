import sys

input = sys.stdin.readline
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    player = []
    ans = 0
    for a in A:
        player.append(0)
        next_player = []

        for p in player:
            if p + a >= 4:
                ans += 1
            else:
                next_player.append(p + a)
        player = next_player
    print(ans)
            


if __name__ == "__main__":
    solve()