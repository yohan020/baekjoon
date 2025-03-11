import sys 
input = sys.stdin.readline

N, S = map(int, input().split())
num_arr = list(map(int, input().split()))

result = 100001
idx1, idx2 = 0,0
temp_sum = num_arr[0]
while True:
    if S <= temp_sum:
        result = min(result, idx1-idx2+1)
    if temp_sum < S:
        idx1 += 1
        temp_sum += num_arr[idx1]
    else:
        temp_sum -= num_arr[idx2]
        idx2 += 1
    if idx1 == N-1 and temp_sum < S:
        break
    
if result == 100001:
    result = 0
print(result)