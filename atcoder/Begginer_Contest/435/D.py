import sys
from collections import deque
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    rev_graph=[[] for _ in range(N+1)]
    black = set()
    for _ in range(M):
        X, Y = map(int, input().split())
        rev_graph[Y].append(X)

    visited = [False] * (N+1)
    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            if not visited[query[1]]:
                visited[query[1]] = True
                queue = deque([query[1]])
                while queue:
                    node = queue.popleft()
                    for next_node in rev_graph[node]:
                        if not visited[next_node]:
                            visited[next_node] = True
                            queue.append(next_node)
        elif query[0] == 2:
            if visited[query[1]]:
                print("Yes")
            else:
                print("No")
            

if __name__ == "__main__":
    solve()