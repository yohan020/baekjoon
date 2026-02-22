import sys

input = sys.stdin.readline

def solve(na, nb, nc):
    return min(na, nc, (na + nb + nc) // 3)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        na, nb, nc = map(int, input().split())
        print(solve(na, nb, nc))