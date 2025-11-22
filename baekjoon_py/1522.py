import sys

input = sys.stdin.readline

def main():
    s = str(input().strip())
    window_size = s.count('a')
    s = s + s
    max_a = 0
    current_a = s[:window_size].count('a')
    max_a = current_a
    for i in range(window_size, len(s)):
        if s[i - window_size] == 'a':
            current_a -= 1
        if s[i] == 'a':
            current_a += 1
        max_a = max(max_a, current_a)
    print(window_size - max_a)

if __name__ == "__main__":
    main()