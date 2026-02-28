import sys

input = sys.stdin.readline
def solve():
    N, Q = map(int, input().split())
    X = list(map(int, input().split()))
    box = [0] * (N + 1)
    res = []
    for x in X:
        if x != 0:
            box[x] += 1
            res.append(x)
        else:
            min_index = 0
            min_value = float('inf')
            for i in range(1, N + 1):
                if box[i] < min_value:
                    min_value = box[i]
                    min_index = i
            box[min_index] += 1
            res.append(min_index)
    print(*res)
    

if __name__ == "__main__":
    solve()