import sys

def solve():
    N, Q = map(int, input().split())
    black = []
    for _ in range(Q):
        L, R = map(int, input().split())
        flag = False
        for interval in black: #검정색 구간을 확장해나가야함
            if (L < interval[0] and interval[0] <= R) or (L <= interval[1] and interval[1] < R):
                interval[0] = min(L, interval[0])
                interval[1] = max(R, interval[1])
                flag = True
                break
            if interval[0] <= L <= interval[1] and interval[0] <= R <= interval[1]:
                flag = True
        if not flag:
            black.append([L, R])
        length = 0
        for interval in black:
            length += interval[1] - interval[0] + 1
        print(N - length, black)


            
                
if __name__ == "__main__":
    solve()