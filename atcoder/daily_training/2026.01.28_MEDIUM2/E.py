import sys

input = sys.stdin.readline
def solve():
    N = int(input().strip())

    ans = []
    
    while N > 0:
        if N % 2 == 1:
            ans.append('A')
            N -= 1
        else:
            ans.append('B')
            N //= 2

    print("".join(ans[::-1]))

if __name__ == "__main__":
    solve()