import sys

input = sys.stdin.readline
def solve():
    Q = int(input())
    snake = []
    first_idx = 0
    diff_idx = 0

    head_ptr = 0

    for _ in range(Q):
        query = list(input().split())
        #print(snake)
        if query[0] == '1':
            x = int(query[1])
            snake.append((x, first_idx))
            first_idx += x
        elif query[0] == '2':
            diff_idx += snake[head_ptr][0]
            head_ptr += 1
        elif query[0] == '3':
            x = int(query[1])
            print(snake[head_ptr + x - 1][1] - diff_idx)
if __name__ == "__main__":
    solve()