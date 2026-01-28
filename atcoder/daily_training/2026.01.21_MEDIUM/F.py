import sys
from collections import deque

input = sys.stdin.readline
def solve():
    Q = int(input())
    q = deque()
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[2]
            q.append((x, query[1]))
        elif query[0] == 2:
            c = query[1]
            ans = 0
            while c > 0:
                x, num = q.popleft()
                if num <= c:
                    ans += x * num
                    c -= num
                else:
                    ans += x * c
                    q.appendleft((x, num - c))
                    c = 0
            print(ans)



if __name__ == "__main__":
    solve()