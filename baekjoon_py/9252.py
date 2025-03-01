s1 = str(input())
s2 = str(input())
l1 = len(s1)
l2 = len(s2)

dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]

for i in range(1, l1+1):
    for j in range(1, l2+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
result = []
i, j = l1, l2  # 마지막 위치에서 시작

#원리 : 인덱스를 감소시킨다는 것은 비교 범위를 줄여가면서 같은 문자가 나오면 결과 배열에 넣는 방식이다
# 결과 배열은 역으로 탐색되어서 요소가 삽입 되므로 마지막에 뒤집어 줘야 한다.
# 그리고 같은 문자가 아닐경우 아직 같은 문자를 찾지 않았으므로 가장 긴 LCS길이를 같는 dp배열의 요소중 큰쪽으로 이동해야 나머지 LCS요소도 찾을 수 있다

while i > 0 and j > 0:
    if s1[i-1] == s2[j-1]:  # 문자가 같으면 LCS에 포함
        result.append(s1[i-1])
        i -= 1
        j -= 1
    elif dp[i-1][j] > dp[i][j-1]:  # 위쪽이 더 크면 위로 이동
        i -= 1
    else:  # 왼쪽이 더 크거나 같으면 왼쪽으로 이동
        j -= 1

result.reverse()  # 역순이므로 뒤집기

print(dp[l1][l2])
print("".join(result))
