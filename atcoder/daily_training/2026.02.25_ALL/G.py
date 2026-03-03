import sys
from collections import defaultdict

input = sys.stdin.readline
def solve():
    N, Q = map(int, input().split())
    
    states = [(-1, "")]

    server_state = 0
    pc_state = [0] * (N + 1)

    for _ in range(Q):
        query = input().rstrip().split()

        if query[0] == '1':
            p = int(query[1])
            pc_state[p] = server_state

        elif query[0] == '2':
            p, s = int(query[1]), query[2]
            new_state_id = len(states)
            states.append((pc_state[p], s))
            pc_state[p] = new_state_id
        
        elif query[0] == '3':
            p = int(query[1])
            server_state = pc_state[p]

    result_parts = []
    curr = server_state

    while curr != 0:
        parent, added_str = states[curr]
        result_parts.append(added_str)
        curr = parent
    result_parts.reverse()
    print(''.join(result_parts))



if __name__ == "__main__":
    solve()