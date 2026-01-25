import sys

input = sys.stdin.readline

def solve():
    T = input().strip()
    U = input().strip()
    for i in range(len(T)-len(U)+1):
        flag = True
        for j in range(i, i + len(U)):
            if T[j] != U[j-i] and T[j] != '?':
                flag = False
                break
        if flag:
            print("Yes")
            return
    print("No")
        


if __name__ == "__main__":
    solve()