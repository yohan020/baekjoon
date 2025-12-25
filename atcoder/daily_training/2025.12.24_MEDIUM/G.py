import sys

# 빠른 입출력 사용
input = sys.stdin.readline

def solve():
    try:
        line = input().strip()
        if not line: return
        N = int(line)
    except ValueError:
        return

    # 좌표의 최댓값이 200,000이므로 넉넉하게 잡습니다.
    MAX_R = 200005
    arr = [0] * (MAX_R + 1)
    
    for _ in range(N):
        L, R = map(int, input().split())
        # [L, R) 구간: 시작점에 +1, 끝점에 -1
        # 인덱스 조작 없이 그대로 사용합니다.
        arr[L] += 1
        arr[R] -= 1
        
    current_sum = 0 # 현재 겹친 구간 수 (S)
    
    ans = []       # 정답 구간들을 저장할 리스트 [(start, end), ...]
    start = -1     # 현재 구간의 시작점 임시 저장
    
    # 0부터 배열 끝까지 순회
    for i in range(len(arr)):
        prev_sum = current_sum
        current_sum += arr[i]
        
        # 1. 구간 시작 감지: 겹친 개수가 0개 -> 1개 이상으로 변하는 순간
        if prev_sum == 0 and current_sum > 0:
            start = i
            
        # 2. 구간 종료 감지: 겹친 개수가 1개 이상 -> 0개로 변하는 순간
        if prev_sum > 0 and current_sum == 0:
            # start부터 현재 i까지가 하나의 합쳐진 구간
            ans.append((start, i))
            
    # 그 다음 k줄에 구간 출력
    for s, e in ans:
        print(s, e)

if __name__ == "__main__":
    solve()