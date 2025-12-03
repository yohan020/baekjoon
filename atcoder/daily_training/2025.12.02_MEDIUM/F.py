import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    S = [list(map(str, input().strip())) for _ in range(N)]
    
    ans = float('inf')

    for target in range(10):
        target_char = str(target)

        indices = []
        for i in range(N):
            idx = S[i].index(target_char)
            indices.append(idx)
        
        count = [0] * 10
        for idx in indices:
            count[idx] += 1
        
        # t초에 멈추는 릴이 K개 있다면, t, t+10, t+20 .... 초에 멈추게 됨
        # 그중 가장 늦게 멈춘 시간은 t + 10 * (count[t]-1)초
        current_max_time = 0
        for t in range(10):
            if count[t] > 0:
                time_needed = t + 10 * (count[t] - 1)
                current_max_time = max(current_max_time, time_needed)
        
        ans = min(ans, current_max_time)
    
    print(ans)

if __name__ == "__main__":
    solve()