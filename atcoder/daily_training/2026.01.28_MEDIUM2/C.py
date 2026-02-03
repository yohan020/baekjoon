import sys

input = sys.stdin.readline
def solve():
    N, M = map(int, input().split())
    bird_cnt = {}
    bird_size = {}
    for _ in range(N):
        A, B = map(int, input().split())
        bird_cnt[A] = bird_cnt.get(A, 0) + 1
        bird_size[A] = bird_size.get(A, 0) + B
    for i in range(1, M + 1):
        print(bird_size[i] / bird_cnt[i])

if __name__ == "__main__":
    solve()