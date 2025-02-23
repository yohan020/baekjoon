#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    int min_result = 987654321;
    int max_result = 0;
    int dp[3][2] = {{0, 0}, {0, 0}, {0, 0}}; // 0-min 1-max , 굳이 다 저장할 필요는 없다 n과 n-1위치만 남기면됨
    int temp[3][2] = {{0, 0}, {0, 0}, {0, 0}}; // n-1부분
    int n[100000][3];
    cin >> N;

    for (int i = 1; i <= N; i++) {
        cin >> n[i][0] >> n[i][1] >> n[i][2];
    }
    for (int i = 1; i <= N; i++) {
        dp[0][0] = min(temp[0][0], temp[1][0]) + n[i][0];
        dp[0][1] = max(temp[0][1], temp[1][1]) + n[i][0];

        dp[1][0] = min(temp[0][0], min(temp[1][0], temp[2][0])) + n[i][1];
        dp[1][1] = max(temp[0][1], max(temp[1][1], temp[2][1])) + n[i][1];

        dp[2][0] = min(temp[1][0], temp[2][0]) + n[i][2];
        dp[2][1] = max(temp[1][1], temp[2][1]) + n[i][2];

        temp[0][0] = dp[0][0];
        temp[0][1] = dp[0][1];
        temp[1][0] = dp[1][0];
        temp[1][1] = dp[1][1];
        temp[2][0] = dp[2][0];
        temp[2][1] = dp[2][1];
    }
    min_result = min(dp[0][0], min(dp[1][0], dp[2][0]));
    max_result = max(dp[0][1], max(dp[1][1], dp[2][1]));
    cout << max_result << " " << min_result;
}
