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
    int dp[100000][3][2]; // 0-min 1-max
    int n[100000][3];
    cin >> N;

    for (int i = 1; i <= N; i++) {
        cin >> n[i][0] >> n[i][1] >> n[i][2];
    }
    //이거 아마 0으로 시작해서 0으로 돌릴 수 있을 듯
    

    for (int i = 1; i <= N; i++) {
        dp[i][0][0] = min(dp[i-1][0][0], dp[i-1][1][0]) + n[i][0];
        dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][1][1]) + n[i][0];

        dp[i][1][0] = min(dp[i-1][0][0], min(dp[i-1][1][0], dp[i-1][2][1])) + n[i][1];
        dp[i][1][1] = max(dp[i-1][0][1], max(dp[i-1][1][1], dp[i-1][2][1])) + n[i][1];

        dp[i][2][0] = min(dp[i-1][1][0], dp[i-1][2][0]) + n[i][2];
        dp[i][2][1] = max(dp[i-1][1][1], dp[i-1][2][1]) + n[i][2];
    }
    min_result = min(dp[N][0][0], min(dp[N][1][0], dp[N][2][0]));
    max_result = max(dp[N][0][1], max(dp[N][1][1], dp[N][2][1]));
    cout << max_result << " " << min_result;
}
