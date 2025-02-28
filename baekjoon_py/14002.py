N = int(input())
num_list = [0] + list(map(int, input().split()))
dp = [1] * (N+1)
path = [0] * (N+1)

for i in range (2, N+1):
    max_idx = 0
    for j in range (1, i):
        if num_list[j] < num_list[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            path[i] = j

max_len = max(dp)
max_idx = 0

for i in range(1, N + 1): #최대 길이가 1일 떄도 다 통함
    if dp[i] == max_len:
        max_idx = i

result = []
while max_idx != 0:
    result.append(num_list[max_idx])
    max_idx = path[max_idx]
result.reverse()

if max_len == 1:
    result.append(num_list[1])

print(max(dp))
print(" ".join(map(str, result)))