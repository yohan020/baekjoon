from queue import PriorityQueue
import sys

input = sys.stdin.readline

def main():
    N = int(input())
    pq = PriorityQueue()
    for _ in range(N):
        num = int(input())
        if num == 0:
            if pq.empty():
                print(0)
            else:
                print(pq.get())
        else:
            pq.put(num)
if __name__ == "__main__":
    main()
