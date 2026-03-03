import sys

input = sys.stdin.readline
# def solve():
#     H, W = map(int, input().split())
#     grid = [input().rstrip() for _ in range(H)]
#     top_idx = 0
#     bottom_idx = H - 1
#     for r in range(H):
#         if '#' in grid[r]:
#             top_idx = r
#             break
#     for r in range(H - 1, -1, -1):
#         if '#' in grid[r]:
#             bottom_idx = r
#             break
#     # 90도 회전
#     rotated_grid = [''.join(grid[r][c] for r in range(H)) for c in range(W)]
#     left_idx = 0
#     right_idx = W - 1
#     for c in range(W):
#         if '#' in rotated_grid[c]:
#             left_idx = c
#             break
#     for c in range(W - 1, -1, -1):
#         if '#' in rotated_grid[c]:
#             right_idx = c
#             break
#     for r in range(top_idx, bottom_idx + 1):
#         for c in range(left_idx, right_idx + 1):
#             if grid[r][c] == '.':
#                 print(r + 1, c + 1)
#                 return
def solve():
    H, W = map(int, input().split())
    grid = [input().rstrip() for _ in range(H)]

    top_idx = next(i for i in range(H) if '#' in grid[i])
    bottom_idx = next(i for i in range(H - 1, - 1, - 1) if '#' in grid[i])

    left_idx = min(row.find('#') for row in grid if '#' in row)
    right_idx = max(row.rfind('#') for row in grid if '#' in row)

    for r in range(top_idx, bottom_idx + 1):
        for c in range(left_idx, right_idx + 1):
            if grid[r][c] == '.':
                print(r + 1, c + 1)
                return

if __name__ == "__main__":
    solve()