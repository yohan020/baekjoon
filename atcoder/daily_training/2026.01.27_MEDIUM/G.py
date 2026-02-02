import sys

input = sys.stdin.readline
def solve():
    N, M = map(int, input().split())
    L = list(map(int, input().split()))

    def check(limit_width):
        line_count = 1
        current_width = 0
        for word_len in L:
            if word_len > limit_width:
                return False
            if current_width == 0:
                current_width += word_len
            else:
                if current_width + 1 + word_len <= limit_width:
                    current_width += 1 + word_len
                else:
                    line_count += 1
                    current_width = word_len
        return line_count <= M
    
    low = max(L)
    high = sum(L) + N

    answer = high

    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    print(answer)

if __name__ == "__main__":
    solve()