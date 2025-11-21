import sys

input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        prices = list(map(int, input().split()))
        max_price = prices[-1]
        profit = 0
        for price in reversed(prices[:-1]):
            if price < max_price:
                profit += max_price - price
            else:
                max_price = price
        print(profit)

if __name__ == "__main__":
    main()