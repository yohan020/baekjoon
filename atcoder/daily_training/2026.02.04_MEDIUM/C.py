import sys

input = sys.stdin.readline
def solve(S: str, T: str) -> bool:
    if len(S) > len(T):
        return False
    
    for i in range(len(S)):
        if S[i] != T[i]:
            return False

    return True

if __name__ == "__main__":
    S = input().strip()
    T = input().strip()
    if solve(S, T):
        print("Yes")
    else:
        print("No")