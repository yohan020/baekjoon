#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> coins;
int dp[100001] = {0, };
int n, k;
bool flag; // 합을 만들 수 있는지에 대한 플래그

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> k;
    coins.assign(n, 0);
    for (int i = 0; i < n; i++) cin >> coins[i];

    dp[0] = 0;
    for (int i = 1; i < coins[0]; i++) {
        dp[i] = -1;
    }
    for (int i = coins[0]; i <= k; i++) {
        flag = false;
        dp[i] = i;
        for (int j = coins.size()-1; j >= 0; j--) {
            if (i < coins[j]) continue;
            if (dp[i - coins[j]] == -1 && !flag) continue;
            else if (dp[i - coins[j]] != -1)
            {
                dp[i] = min(dp[i-coins[j]] + 1, dp[i]);
                flag = true;
            }
        }
        if (!flag) {
            dp[i] = -1;
        }
    }
    cout << endl << dp[k];
}