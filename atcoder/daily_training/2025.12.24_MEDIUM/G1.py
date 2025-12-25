import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    arr = [0] * (2*(10**5)+5)

    for _ in range(N):
        L, R = map(int, input().split())
        arr[L] += 1
        arr[R] -= 1
    ans = []
    start = -1
    current_s = 0
    for i in range(len(arr)):
        prev_s = current_s
        current_s += arr[i]
        if prev_s == 0 and current_s > 0:
            start = i
        elif prev_s > 0 and current_s == 0:
            ans.append((start, i))
    for s, e in ans:
        print(s, e)

if __name__ == "__main__":
    solve()
    
