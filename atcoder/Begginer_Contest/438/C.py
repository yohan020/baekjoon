import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    stack = []
    for x in A:
        if stack and stack[-1][0] == x:
            stack[-1][1] += 1  # 개수 증가
            
            if stack[-1][1] == 4:
                stack.pop()
        else:
            stack.append([x, 1])

    ans = 0
    for val, count in stack:
        ans += count
        
    print(ans)
    
if __name__ == "__main__":
    solve()