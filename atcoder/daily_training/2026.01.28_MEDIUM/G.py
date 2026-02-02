import sys

input = sys.stdin.readline

def solve():
    # N: 사람 수, M: 둘레, C: 목표 인원
    line1 = input().split()
    if not line1: return
    N, M, C = map(int, line1)
    
    A = list(map(int, input().split()))

    stage = {}
    for pos in A:
        stage[pos] = stage.get(pos, 0) + 1
    
    unique_locs = sorted(stage.keys())

    unique_locs_ext = unique_locs + [ x + M for x in unique_locs]
    counts_ext = [stage[x] for x in unique_locs] * 2

    total_len = len(unique_locs)

    ans = 0
    right = 0
    current_people_sum = 0

    for left in range(total_len):
        while right < len(unique_locs_ext) and current_people_sum < C:
            current_people_sum += counts_ext[right]
            right += 1

        curr_loc = unique_locs_ext[left]
        if left == 0:
            # 이떄 prev는 음수가 됨
            # 왜냐? 마지막위치에서 0으로 돌아오는 거리 -> 음수
            prev_loc = unique_locs[-1] - M
        else:
            # unique_locs_ext를 쓰는이유는 right가 한바퀴넘어서 돌아갈 수 있기 떄문
            prev_loc = unique_locs_ext[left - 1]

        gap = curr_loc - prev_loc

        ans += gap * current_people_sum

        current_people_sum -= counts_ext[left]

    print(ans)

if __name__ == "__main__":
    solve()