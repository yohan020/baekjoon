import sys

# 빠른 입력을 위해 사용
input = sys.stdin.readline

def solve():
    # 줄바꿈 문자 제거를 위해 strip() 필수
    line = input().strip()
    if not line: return # 예외 처리
    N = int(line)
    S = input().strip()

    # dp[손] = 현재 판에 해당 '손'을 냈을 때까지의 최대 승리 횟수
    # 초기값 0으로 시작 (첫 판은 이전 제약이 없으므로)
    dp = {'R': 0, 'P': 0, 'S': 0}

    for s in S:
        new_dp = {'R': -1, 'P': -1, 'S': -1} # 이번 턴의 결과를 담을 임시 dp
        
        # 아오키의 수에 따라 이기는 손(win)과 비기는 손(draw) 결정
        # 지는 손은 낼 수 없으므로 고려하지 않음
        if s == 'R':
            win_hand, draw_hand = 'P', 'R'
        elif s == 'P':
            win_hand, draw_hand = 'S', 'P'
        else: # s == 'S'
            win_hand, draw_hand = 'R', 'S'
            
        # 1. 이번에 '이기는 손'을 내는 경우
        # 이전 판(prev)에 '이기는 손'과 다른 손을 냈어야 함
        max_prev_win = -1
        for h in ['R', 'P', 'S']:
            if h != win_hand: # 연속된 손 금지 조건
                max_prev_win = max(max_prev_win, dp[h])
        
        if max_prev_win != -1:
            new_dp[win_hand] = max_prev_win + 1 # 승리했으므로 +1
            
        # 2. 이번에 '비기는 손'을 내는 경우
        # 이전 판(prev)에 '비기는 손'과 다른 손을 냈어야 함
        max_prev_draw = -1
        for h in ['R', 'P', 'S']:
            if h != draw_hand: # 연속된 손 금지 조건
                max_prev_draw = max(max_prev_draw, dp[h])
        
        if max_prev_draw != -1:
            new_dp[draw_hand] = max_prev_draw # 승수가 늘지 않음 (+0)

        # dp 갱신
        dp = new_dp

    # 마지막 판까지 왔을 때, R/P/S 중 가장 많이 이긴 횟수 출력
    print(max(dp.values()))

if __name__ == "__main__":
    solve()