import sys
from collections import deque

input = sys.stdin.readline
def solve():
    Q = int(input())
    snake = deque()
    
    current_tail_pos = 0

    minus_coord = 0

    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            l = query[1]
            snake.append((current_tail_pos, l))
            current_tail_pos += l
        elif query[0] == 2:
            popped_snake = snake.popleft()
            length = popped_snake[1]

            minus_coord += length

            if not snake:
                current_tail_pos = 0
                minus_coord = 0
        elif query[0] == 3:
            k = query[1]
            original_pos = snake[k - 1][0]
            print(original_pos - minus_coord)
            

if __name__ == "__main__":
    solve()