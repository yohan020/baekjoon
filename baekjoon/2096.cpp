#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    int dp[3][2];
    int temp[3][2];
    int n[100000][3];
    cin >> N;

    memset(dp, 0,sizeof(dp));
    memset(temp, 0,sizeof(temp));

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

        for (int j = 0; j < 3; j++) {
            for (int k = 0; k < 2; k++) {
                temp[j][k] = dp[j][k];
            }
        }
    }
    cout << max(dp[0][1], max(dp[1][1], dp[2][1])) << " " << min(dp[0][0], min(dp[1][0], dp[2][0]));
}
