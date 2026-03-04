import sys

input = sys.stdin.readline
# def solve():
#     N, X = map(int, input().split())
#     reachable = {0}

#     for _ in range(N):
#         a, b = map(int, input().split())
#         new_reachable = set()

#         for pos in reachable:
#             if pos + a <= X:
#                 new_reachable.add(pos + a)
#             if pos + b <= X:
#                 new_reachable.add(pos + b)
        
#         reachable = new_reachable

#         if not reachable:
#             break
#     if X in reachable:
#         print("Yes")
#     else:
#         print("No")
def solve():
    N, X = map(int, input().split())
    nums = [tuple(map(int, input().split())) for _ in range(N)]

    memo = {}

    def dfs(i, total):
        if total > X:
            return False
        if i == N:
            return total == X
        state = (i, total)

        if state in memo:
            return memo[state]
        
        res = dfs(i + 1, total + nums[i][0]) or dfs(i + 1, total + nums[i][1])

        memo[state] = res
        return res
    if dfs(0, 0):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()