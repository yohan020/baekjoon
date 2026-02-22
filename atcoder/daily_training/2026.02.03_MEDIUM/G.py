import sys
import heapq

input = sys.stdin.readline
def solve():
    N, K = map(int, input().split())
    customers = []
    for _ in range(N):
        A, B, C = map(int, input().split())
        customers.append((A, B, C))
    
    time = 0
    seated_customers = 0
    store = []

    for customer in customers:
        A, B, C = customer
        while store and seated_customers + C > K:
            leave_time, leave_customer = heapq.heappop(store)
            time = leave_time
            seated_customers -= leave_customer
        time = max(time, A)
        print(time)
        seated_customers += C
        heapq.heappush(store, (time + B, C))
if __name__ == "__main__":
    solve()