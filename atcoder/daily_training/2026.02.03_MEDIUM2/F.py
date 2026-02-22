import sys

input = sys.stdin.readline
def solve():
    N, M = map(int, input().split())
    death_pos = set()
    moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
    for _ in range(M):
        a, b = map(int, input().split())
        death_pos.add((a, b))
        for dx, dy in moves:
            na, nb = a + dx, b + dy
            if 1 <= na <= N and 1 <= nb <= N:
                death_pos.add((na, nb))

    print(N*N - len(death_pos))
    

if __name__ == "__main__":
    solve()