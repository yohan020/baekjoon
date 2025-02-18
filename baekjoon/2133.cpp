#include <iostream>

using namespace std;


int main(void)
{
    int dp[31] = {0, };
    int N;
    cin >> N;

    dp[0] = 1;
    dp[2] = 3;
    for (int i = 4; i <= N; i += 2) {
        dp[i] = dp[i - 2] * 4 - dp[i - 4];
    }
    cout << dp[N];
}