import sys

input = sys.stdin.readline
def solve():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    
    rev_num = [0] * (N + 1)
    for i in range(N):
        number_on_shirt = Q[i]
        rev_num[number_on_shirt] = i

    res = []
    for i in range(1, N + 1):
        person_idx = rev_num[i]

        target_person_num = P[person_idx]
        target_person_idx = target_person_num - 1

        target_shirt_num = Q[target_person_idx]

        res.append(target_shirt_num)
    print(*res)
if __name__ == "__main__":
    solve()