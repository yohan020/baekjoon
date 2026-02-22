import sys

input = sys.stdin.readline

def get_black_cells(H, W, grid):
    cells = set()
    for r in range(H):
        for c in range(W):
            if grid[r][c] == '#':
                cells.add((r, c))
    return cells

def solve():
    H_A, W_A = map(int, input().split())
    A = [input().strip() for _ in range(H_A)]

    H_B, W_B = map(int, input().split())
    B = [input().strip() for _ in range(H_B)]

    H_X, W_X = map(int, input().split())
    X = [input().strip() for _ in range(H_X)]

    A_cells = get_black_cells(H_A, W_A, A)
    B_cells = get_black_cells(H_B, W_B, B)
    X_cells = get_black_cells(H_X, W_X, X)

    for dr_A in range(-H_A, H_X + 1):
        for dc_A in range(-W_A, W_X + 1):
            shifted_A = {(r + dr_A, c + dc_A) for r, c in A_cells}

            valid_A = True

            for r, c in shifted_A:
                if not (0 <= r < H_X and 0 <= c < W_X):
                    valid_A = False
                    break
            
            if not valid_A:
                continue

            for dr_B in range(-H_B, H_X + 1):
                for dc_B in range(-W_B, W_X + 1):

                    shifted_B = {(r + dr_B, c + dc_B) for r, c in B_cells}

                    valid_B = True
                    for r, c in shifted_B:
                        if not (0 <= r < H_X and 0 <= c < W_X):
                            valid_B = False
                            break

                    if not valid_B:
                        continue
                        
                    if shifted_A | shifted_B == X_cells:
                        print("Yes")
                        return
    print("No")
if __name__ == "__main__":
    solve()