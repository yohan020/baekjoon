import sys

input = sys.stdin.readline

def main():
    n = int(input())
    word = str(input().strip())

    cnt = [0] * 27
    l = len(word)
    for i in word:
        cnt[ord(i) - ord('A')] += 1
    answer = 0
    for _ in range(n - 1):
        temp = str(input().strip())
        if abs(len(temp)-l) > 1:
            continue
        temp_cnt = [0] * 27
        for i in temp:
            temp_cnt[ord(i) - ord('A')] += 1
        diff = 0
        for i in range(26):
            diff += abs(cnt[i] - temp_cnt[i])
        if diff <= 2:
            answer += 1
    print(answer)

    

if __name__ == "__main__":
    main()