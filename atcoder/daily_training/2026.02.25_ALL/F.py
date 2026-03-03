import sys

input = sys.stdin.readline

def check_dots(grid):
    dots_positions = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '#':
                dots_positions.append((i, j))
    
    if not dots_positions:
        return []
    
    std_pos_i, std_pos_j = dots_positions[0]
    return [(i - std_pos_i, j - std_pos_j) for i, j in dots_positions]

def solve():
    global N
    N = int(input())
    S = [list(input().rstrip()) for _ in range(N)]
    T = [list(input().rstrip()) for _ in range(N)]

    S_dots = 0
    T_dots = 0
    for i in range(N):
        S_dots += S[i].count('#')
        T_dots += T[i].count('#')
    if S_dots != T_dots:
        print('No')
        return
    
    T_dots_positions = check_dots(T)

    for _ in range(4):
        S_dots_positions = check_dots(S)
        if S_dots_positions == T_dots_positions:
            print('Yes')
            return
        # Rotate S 90 degrees clockwise
        S = [list(row) for row in zip(*S[::-1])]

    print('No')
        


if __name__ == "__main__":
    solve()