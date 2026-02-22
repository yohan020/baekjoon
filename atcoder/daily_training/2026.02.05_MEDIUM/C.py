import sys

input = sys.stdin.readline
def solve(query: list, player: list) -> None:
    if query[0] == 1:
        player[query[1]] += 1
    elif query[0] == 2:
        player[query[1]] += 2
    elif query[0] == 3:
        if player[query[1]] >= 2:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    N, Q = map(int, input().split())
    player = [0] * (N + 1)
    for _ in range(Q):
        query = list(map(int, input().split()))
        solve(query, player)