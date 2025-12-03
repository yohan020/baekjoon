import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    # strip()을 해야 개행문자가 제거됨
    S = list(input().strip())
    Q = int(input())
    
    # 각 문자가 마지막으로 수정된 시점 (초기값은 -1)
    last_update_time = [-1] * N
    
    # 마지막 전체 변환 명령: (시간, 종류)
    # 종류: 0=없음, 2=소문자로, 3=대문자로
    last_global_op = (-1, 0) 
    
    for t in range(Q):
        query = input().split()
        if query[0] == '1':
            idx = int(query[1]) - 1
            char = query[2]
            S[idx] = char
            last_update_time[idx] = t
        elif query[0] == '2':
            # 소문자로 변환 명령 (lazy)
            last_global_op = (t, 2)
        elif query[0] == '3':
            # 대문자로 변환 명령 (lazy)
            last_global_op = (t, 3)
            
    # 최종 출력 시점
    global_time, global_type = last_global_op
    
    for i in range(N):
        # 만약 해당 문자의 마지막 수정 시간이 전체 변환 명령 시간보다 이전이라면
        # 전체 변환을 적용해야 함
        if last_update_time[i] < global_time:
            if global_type == 2:
                S[i] = S[i].lower()
            elif global_type == 3:
                S[i] = S[i].upper()
                
    print(''.join(S))

if __name__ == "__main__":
    solve()