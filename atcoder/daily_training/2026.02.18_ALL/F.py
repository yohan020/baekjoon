import sys
from collections import Counter, defaultdict

input = sys.stdin.readline
# def solve():
#     N = int(input())
#     A = list(map(int, input().split()))
#     c = Counter(A)
#     temp = defaultdict(int)
#     nums = sorted(list(set(A)), reverse=True)
#     for i in range(1, len(nums)):
#         temp[nums[i]] = temp[nums[i - 1]] + nums[i - 1] * c[nums[i - 1]]
#     res = []
#     for a in A:
#         res.append(temp[a])
#     print(*res)

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    sorted_A = sorted(A, reverse=True)

    greater_sum = {}
    current_sum = 0
    
    for a in sorted_A:
        if a not in greater_sum:
            greater_sum[a] = current_sum
        current_sum += a
    
    res = [greater_sum[a] for a in A]
    print(*res)

if __name__ == "__main__":
    solve()