import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    score = list(map(int, input().split()))
    res = 0
    
    for s in score:
        found = False
        for a in range(1, 251):
            for b in range(1, 251):
                temp = 4 * a * b + 3 * a + 3 * b
                if temp == s:
                    res += 1
                    found = True
                    break
                if temp > s:
                    break
            if found:
                break
    print(N-res)

if __name__ == "__main__":
    solve()