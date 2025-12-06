import sys

input = sys.stdin.readline

def solve():
    A, B = map(list, input().split())
    reversed_A = A[::-1]
    reversed_B = B[::-1]
    min_len = min(len(reversed_A), len(reversed_B))
    for i in range(min_len):
        if int(reversed_A[i]) + int(reversed_B[i]) >= 10:
            print('Hard')
            return
    print('Easy')

if __name__ == "__main__":
    solve()