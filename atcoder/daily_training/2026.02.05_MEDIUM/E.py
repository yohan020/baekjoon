import sys

input = sys.stdin.readline
def solve(N: int, M: int, A: str) -> int:
    max_logo_needed = 0

    current_plain = M
    current_logo_used = 0

    for plan in A:
        if plan == '0':
            current_plain = M
            current_logo_used = 0
        elif plan == '1':
            if current_plain > 0:
                current_plain -= 1
            else:
                current_logo_used += 1
        elif plan == '2':
            current_logo_used += 1
        if current_logo_used > max_logo_needed:
            max_logo_needed = current_logo_used
    return max_logo_needed

if __name__ == "__main__":
    N, M = map(int, input().split())
    A = input().strip()
    print(solve(N, M, A))