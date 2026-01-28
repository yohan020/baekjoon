import sys

def Counter(lst):
    cnt = {}
    for n in lst:
        if n in cnt:
            cnt[n] += 1
        else:
            cnt[n] = 1
    return cnt

input = sys.stdin.readline
def solve():
    N = int(input())
    dice = []
    for _ in range(N):
        data = list(map(int, input().split()))
        face = data[1:]
        dice.append(face)
    
    max_prob = 0.0

    for i in range(N):
        for j in range(i + 1, N):

            count_i = Counter(dice[i])
            count_j = Counter(dice[j])

            total_matches = 0
            for num in count_i:
                if num in count_j:
                    total_matches += count_i[num] * count_j[num]
            
            total_cases = len(dice[i]) * len(dice[j])
            prob = total_matches / total_cases
            max_prob = max(max_prob, prob)
    print(max_prob)


if __name__ == "__main__":
    solve()