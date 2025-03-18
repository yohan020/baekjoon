import math

# 입력: X, Y (현재 좌표), D (점프 거리), T (점프에 걸리는 시간)
X, Y, D, T = map(int, input().split())

# (0, 0)까지의 유클리드 거리
d = math.sqrt(X**2 + Y**2)

# 기본 후보: 전부 걸어가는 시간
ans = d

# d가 D보다 작을 경우
if d < D:
    ans = min(ans, T + (D - d), 2 * T)
else:
    n = int(d // D)  # 최대 점프 횟수
    r = d - n * D    # 점프 후 남은 거리
    # 후보 1: n번 점프 후 나머지 걸어감
    candidate1 = n * T + r
    # 후보 2: 한 번 더 점프하는 경우
    candidate2 = (n + 1) * T
    ans = min(ans, candidate1, candidate2)

print(float(ans))
