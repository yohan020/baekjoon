import sys

input = sys.stdin.readline
def solve():
    N = int(input())
    S = input().rstrip()
    max_len = float('-inf')

    for i in range(N):
        if S[i] == '/':
            left = i - 1
            right = i + 1
            current_len = 1

            while left >= 0 and right < N and S[left] == '1' and S[right] == '2':
                current_len += 2
                left -= 1
                right += 1
            max_len = max(max_len, current_len)
    print(max_len)

if __name__ == "__main__":
    solve()