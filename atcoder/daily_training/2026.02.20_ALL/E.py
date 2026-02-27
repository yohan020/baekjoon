import sys

input = sys.stdin.readline
def solve():
    N = int(input())
    slot = []
    for _ in range(N):
        slot.append(input().rstrip())
    
    ans = float('inf')

    for i in range(10):
        target_char = str(i)

        counts = [0] * 10

        for s in slot:
            idx = s.index(target_char)
            counts[idx] += 1
        
        max_time = 0
        for j in range(10):
            needed_time = j + 10 * (counts[j] - 1)
            max_time = max(max_time, needed_time)
        ans = min(ans, max_time)

    print(ans)
if __name__ == "__main__":
    solve()