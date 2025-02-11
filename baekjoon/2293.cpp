#include <iostream>
#include <vector>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int dp[10001] = {0, };
    int n, k;
    cin >> n >> k;

    vector <int> coins(n);
    for (int i = 0; i < n; i++) cin >> coins[i];

    dp[0] = 1;
    for (int coin: coins) {
        for (int i = coin; i <=k ;i++) {
            dp[i] += dp[i-coin];
        }
    }
    cout << dp[k];
}