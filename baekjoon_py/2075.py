import heapq
import sys

input = sys.stdin.readline
def main():
    N = int(input())
    hp = []
    for _ in range(N):
        num = list(map(int, input().split()))
        for n in num:
            if len(hp) < N:
                heapq.heappush(hp, n)
            else:
                if hp[0] < n:
                    heapq.heappop(hp)
                    heapq.heappush(hp, n)
    print(hp[0])
        
if __name__ == "__main__":
    main()