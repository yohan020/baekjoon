import sys

input = sys.stdin.readline
def solve():
    T = int(input())

    for _ in range(T):
        N, H = map(int, input().split())

        targets = []
        for _ in range(N):
            targets.append(list(map(int, input().split())))
        
        targets.sort(key=lambda x: x[0])

        now_t = 0
        min_h = H
        max_h = H
        possible = True

        for t, l, u in targets:
            dt = t - now_t

            next_min_h = min_h - dt
            next_max_h = max_h + dt

            real_min = max(next_min_h, l)
            real_max = min(next_max_h, u)

            if real_min > real_max:
                possible = False
                break

            min_h = real_min
            max_h = real_max
            now_t = t
        print("Yes" if possible else "No")
if __name__ == "__main__":
    solve()