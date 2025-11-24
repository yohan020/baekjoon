import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    words = {}
    ans = N
    for _ in range(N):
        word = input().strip()
        words[word] = 1
    for _ in range(M):
        sentence = list(input().strip().split(','))
        for word in sentence:
            if word in words:
                words.pop(word)
                ans -= 1
        print(ans)
        
if __name__ == "__main__":
    main()