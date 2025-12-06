import sys
from bisect import bisect_right, bisect_left
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    A.sort()
    B.sort()

    prices = sorted(list(set(A+B)))

    for p in prices:
        cnt_A = bisect_right(A, p) #정렬된 A에서 p가 들어갈 수 있는 가장 오른쪽 인덱스
        cnt_B = M - bisect_left(B, p) #정렬된 B에서 p가 들어갈 수 있는 가장 왼쪽 인덱스
        if cnt_A >= cnt_B:
            print(p)
            return
        else:
            cnt_A = bisect_right(A, p+1) #정렬된 A에서 p가 들어갈 수 있는 가장 오른쪽 인덱스
            cnt_B = M - bisect_left(B, p+1) #정렬된 B에서 p가 들어갈 수 있는 가장 왼쪽 인덱스
            if cnt_A >= cnt_B:
                print(p+1)
                return

if __name__ == "__main__":
    solve()