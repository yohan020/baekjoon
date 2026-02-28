import sys
from collections import deque

input = sys.stdin.readline
def solve():
    N, X, Y = map(int, input().split())
    tree = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    visited = [-1] * (N + 1)
    visited[X] = 0
    dq = deque([X])
    while dq:
        node = dq.popleft()
        if node == Y:
            path = []
            while node != 0:
                path.append(node)
                node = visited[node]
            print(*path[::-1])
            return
        for next_node in tree[node]:
            if visited[next_node] == -1:
                visited[next_node] = node
                dq.append(next_node)
if __name__ == "__main__":
    solve()