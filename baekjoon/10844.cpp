#include <iostream>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    int result = 0;
    long long dp[101][11] = {0, };
    cin >> N;

    dp[1][0] = 1;
    dp[1][10] = 0;
    for (int i = 1; i < 10; i++) {
        dp[1][i] = 1;
    }
    for (int i = 2; i <= N; i++) {
        for (int j = 0; j < 10; j++) {
            if (j == 0) dp[i][j] = dp[i-1][1];
            else dp[i][j] = (dp[i-1][j - 1] + dp[i-1][j+1]) % 1000000000;
        }
    }
    for (int i = 1; i < 10; i++) {
        result = (result + dp[N][i]) % 1000000000;
    }
    cout << result;
}