import sys

input = sys.stdin.readline

def main(): 
    N, M = map(int, input().split())
    strengths = []
    for _ in range(N):
        name, power = input().split()
        strengths.append((name, int(power)))
    result = []
    for _ in range(M):
        power = int(input())
        left = 0
        right = N - 1
        while left < right:
            mid = (left + right) // 2
            if strengths[mid][1] >= power:
                right = mid
            else:
                left = mid + 1
        result.append(strengths[left][0])
    print("\n".join(result))
if __name__ == "__main__":
    main()