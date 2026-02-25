import sys

input = sys.stdin.readline
def solve():
    S = list(input().rstrip())
    T = list(input().rstrip())
    if S == T:
        print("Yes")
        return
    for i in range(1, len(T)):
        temp = S.copy()
        t = temp[i]
        temp[i] = temp[i - 1]
        temp[i - 1] = t
        if temp == T:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    solve()