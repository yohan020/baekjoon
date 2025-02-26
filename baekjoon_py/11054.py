N = int(input())
num_list = [0] + list(map(int, input().split()))

dp1 = [1] * (N+1)
dp2 = [1] * (N+1)

dp1[1] = 1
for i in range(1, N+1):
    for j in range(1, i+1):
        if (num_list[j] < num_list[i]): 
            dp1[i] = max(dp1[j] + 1, dp1[i])
for i in range(N, 0, -1):
    for j in range(N, i, -1):
        if (num_list[j] < num_list[i]):
            dp2[i] = max(dp2[j] + 1, dp2[i])

result = [a + b for a, b in zip(dp1, dp2)]
print(max(result) - 1)