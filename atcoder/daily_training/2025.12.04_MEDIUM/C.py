import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    candidates = []
    for i in range(1, N+1):
        C = int(input())
        A = list(map(int, input().split()))
        candidates.append({'id':i, 'count':C, 'nums':A})
    X = int(input())
    winner = []
    for i in candidates:
        if X in i['nums']:
            winner.append(i)
    if not winner:
        print(0)
        return
    min_len = min(i['count'] for i in winner)
    final_result = [i['id'] for i in winner if i['count'] == min_len]
    final_result.sort()
    print(len(final_result))
    for i in final_result:
        print(i, end=' ')

if __name__ == "__main__":
    solve()