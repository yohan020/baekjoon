import sys

input = sys.stdin.readline

def solve():
    N = 3
    M = int(input())  # 문자열 길이
    S = [input().strip() for _ in range(N)]  # 3개의 릴 문자열
    
    
    min_total_time = float('inf')  # 정답(최솟값) 저장용
    found_any = False # 불가능 여부 체크

    # 1. 숫자 0부터 9까지 시도 ('0' ~ '9')
    for target in range(10):
        target_char = str(target)
        
        # 모든 릴에 해당 숫자가 있는지 확인
        if not (target_char in S[0] and target_char in S[1] and target_char in S[2]):
            continue
        
        found_any = True
        
        # 2. 각 릴에서 target 문자가 있는 '모든 인덱스' 수집
        indices = []
        for i in range(3):
            pos_list = [j for j, char in enumerate(S[i]) if char == target_char]
            indices.append(pos_list)
            
        # 3. 가능한 모든 위치 조합을 시도 (완전 탐색)
        # 예: 릴1은 첫번째 '7', 릴2는 두번째 '7'을 쓸 경우 등
        import itertools
        current_digit_min_time = float('inf')
        
        for p1 in indices[0]:
            for p2 in indices[1]:
                for p3 in indices[2]:
                    # 선택된 인덱스들: [p1, p2, p3]
                    # 같은 인덱스가 몇 개인지 카운트해서 추가 시간(M) 계산
                    
                    # 충돌 해결 로직
                    times = [p1, p2, p3]
                    # 같은 값이 있으면 M씩 더해줘야 함.
                    # 간단한 방법: 값을 정렬하고, 앞의 값과 같으면 +M 누적
                    times.sort()
                    
                    actual_times = []
                    for t in times:
                        # 이미 actual_times에 t가 있다면 t+M, t+2M... 으로 변경
                        while t in actual_times:
                            t += M
                        actual_times.append(t)
                    
                    # 셋 중 가장 늦게 끝나는 시간이 이 조합의 소요 시간
                    max_time = max(actual_times)
                    current_digit_min_time = min(current_digit_min_time, max_time)

        # 전체 정답 갱신
        min_total_time = min(min_total_time, current_digit_min_time)

    if not found_any or min_total_time == float('inf'):
        print(-1)
    else:
        print(min_total_time)

if __name__ == "__main__":
    solve()
