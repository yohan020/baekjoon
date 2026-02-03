import sys

# 입력 속도 가속
input = sys.stdin.readline

def solve():
    # 입력 받기
    N, A, B = map(int, input().split())
    S = input().strip()

    count_a_for_left_a = 0  # a 조건 확인용 윈도우의 a 개수
    count_b_for_left_b = 0  # b 조건 확인용 윈도우의 b 개수
    
    left_a = 0 # 'a' 개수 조건을 만족하는 구간의 "끝" (exclusive)
    left_b = 0 # 'b' 개수 조건을 만족하는 구간의 "시작" (inclusive)
    
    ans = 0


    for right in range(N):

        char = S[right]
        

        if char == 'a':
            count_a_for_left_a += 1
        
        if char == 'b':
            count_b_for_left_b += 1
            
        while count_b_for_left_b >= B:
            if S[left_b] == 'b':
                count_b_for_left_b -= 1
            left_b += 1
            
        while count_a_for_left_a >= A:
            if S[left_a] == 'a':
                count_a_for_left_a -= 1
            left_a += 1
                    
        term = left_a - left_b
        if term > 0:
            ans += term

    print(ans)

if __name__ == "__main__":
    solve()