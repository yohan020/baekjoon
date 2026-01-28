import sys

input = sys.stdin.readline
def solve():
    N = int(input())
    is_login = False
    error = 0
    for _ in range(N):
        action = input().strip()
        if action == 'login':
            is_login = True
        elif action == 'logout':
            is_login = False
        elif action == 'private':
            if not is_login:
                error += 1
    print(error)


if __name__ == "__main__":
    solve()