import sys

input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        n, k, t, m = list(map(int, input().split()))
        scores = {i: [0] * (k + 1) for i in range(1, n + 1)}
        cnt = [0] * (n + 1)
        order = [0] * (n + 1)
        for idx in range(m):
            i, j, s = list(map(int, input().split()))
            scores[i][j] = max(scores[i][j], s)
            cnt[i] += 1
            order[i] = idx
        print(sorted(scores, key=lambda x: [-sum(scores[x]), cnt[x], order[x]]).index(t) + 1)
        

if __name__ == "__main__":
    main()