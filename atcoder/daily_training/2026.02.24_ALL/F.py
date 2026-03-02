import sys

input = sys.stdin.readline
def solve():
    N = int(input())
    P = list(map(int, input().split()))

    signs = []
    for i in range(N - 1):
        signs.append(P[i] < P[i + 1])
    
    rle = []
    current_sign = signs[0]
    count = 1

    for i in range(1, len(signs)):
        if signs[i] == current_sign:
            count += 1
        else:
            rle.append((current_sign, count))
            current_sign = signs[i]
            count = 1
    rle.append((current_sign, count))

    ans = 0
    for i in range(len(rle) - 2):
        if rle[i][0] == True and rle[i + 1][0] == False and rle[i + 2][0] == True:
            left_plus = rle[i][1]
            right_plus = rle[i + 2][1]

            ans += left_plus * right_plus
    print(ans)
        


if __name__ == "__main__":
    solve()