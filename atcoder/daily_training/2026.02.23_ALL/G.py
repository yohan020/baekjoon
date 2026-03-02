import sys
from collections import deque

input = sys.stdin.readline
def solve():
    N = int(input())
    S = input().rstrip() + '..'
    T = input().rstrip() + '..'

    if S.count('W') != T.count('W'):
        print(-1)
        return
    

    visited = {S : 0}
    queue = deque([S])

    while queue:
        current = queue.popleft()
        if current == T:
            print(visited[current])
            return
        
        empty_idx = current.find('..')
        for i in range(N + 1):
            if current[i] != '.' and current[i + 1] != '.':
                next_state = list(current)
                next_state[empty_idx], next_state[empty_idx + 1] = next_state[i], next_state[i + 1]
                next_state[i], next_state[i + 1] = '.', '.'
                next_state = ''.join(next_state)
                if next_state not in visited:
                    visited[next_state] = visited[current] + 1
                    queue.append(next_state)
    print(-1)
                
    

if __name__ == "__main__":
    solve()