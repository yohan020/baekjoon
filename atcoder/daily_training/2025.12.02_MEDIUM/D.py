import sys
from collections import deque

input = sys.stdin.readline
def solve():
    Q = int(input())
    que = deque()
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            que.appendleft(query[1])
        elif query[0] == 2:
            print(que.pop())
        
if __name__ == "__main__":
    solve()