import sys

input = sys.stdin.readline

def palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True

def solve():
    S = input().strip()
    if palindrome(S):
        print("Yes")
        return
    front_a_cnt = 0
    back_a_cnt = 0
    for i in range(len(S)):
        if S[i] == 'a':
            front_a_cnt += 1
        else:
            break
    for i in range(len(S)):
        if S[-i-1] == 'a':
            back_a_cnt += 1
        else:
            break
    S = 'a' * (abs(front_a_cnt-back_a_cnt)) + S
    if palindrome(S):
        print("Yes")
        return
    print("No")
    


    

if __name__ == "__main__":
    solve()