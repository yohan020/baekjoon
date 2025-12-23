import sys

input = sys.stdin.readline

def solve():
    N, R, C = map(int, input().split())
    wind = input().strip()
    
    visited = set()
    visited.add((0,0))

    curr_r, curr_c = 0, 0

    ans = []

    for i in wind:
        if i == 'N':
            curr_r -= 1
        elif i == 'S':
            curr_r += 1
        elif i == 'W':
            curr_c -= 1
        elif i == 'E':
            curr_c += 1
        
        target = (curr_r - R, curr_c - C)
        if target in visited:
            ans.append('1')
        else:
            ans.append('0')
        visited.add((curr_r, curr_c))
    
    print(''.join(ans))
if __name__ == "__main__":
    solve()