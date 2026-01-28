import sys

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    power = 1
    cnt = 0
    for domino in A:
        power -= 1
        power = max(power, domino-1)
        cnt += 1
        if power == 0:
            break
    print(cnt)

if __name__ == "__main__":
    solve()
//ㅇㄹㄴㄴ