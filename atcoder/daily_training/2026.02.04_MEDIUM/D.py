import sys

input = sys.stdin.readline
def solve(S: str) -> int:
    substring = set()
    for i in range(1, len(S) + 1):
        for j in range(len(S) - i + 1):
            substring.add(S[j : j + i])

    return len(substring)

if __name__ == "__main__":
    S = input().strip()
    print(solve(S))